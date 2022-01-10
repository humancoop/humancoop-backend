import smtplib
from email.message import EmailMessage
from .schemas import MemberRequest
import logging
import os

logger = logging.getLogger(__name__)


class EmailService:
    @staticmethod
    def _get_subject(request):
        if isinstance(request, MemberRequest):
            return "Nuevo miembro"
        return "Nueva donación"

    @staticmethod
    def _get_recipient() -> str:
        return os.getenv("RECIPIENT_EMAIL")

    @staticmethod
    def _get_sender() -> str:
        return os.getenv("WEBSITE_EMAIL")

    @staticmethod
    def _get_body(request):
        return str(request)

    def send_email(request):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(
                EmailService._get_sender(), os.getenv("WEBSITE_EMAIL_PASSWORD")
            )
            msg = EmailMessage()
            msg.set_content(EmailService._get_body(request))
            msg["Subject"] = EmailService._get_subject(request)
            msg["From"] = EmailService._get_sender()
            msg["To"] = EmailService._get_recipient()

            server.send_message(msg)
            server.close()
            logger.info(f"Email sent to {EmailService._get_recipient()}")
        except Exception as e:
            logger.error("Error sending email: %s", e)
