import smtplib
from email.message import EmailMessage
from .schemas import MemberRequest
from .email_formatter import EmailFormatter
import logging
import os
import boto3
from botocore.exceptions import ClientError

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
        return EmailFormatter.format_email_for_request(request)

    @staticmethod
    def _send_email_using_amazon_ses(request):
        client = boto3.client("ses", region_name="eu-west-3")
        try:
            response = client.send_email(
                Destination={
                    "ToAddresses": [EmailService._get_recipient()],
                },
                Message={
                    "Body": {
                        "Text": {
                            "Charset": "UTF-8",
                            "Data": EmailService._get_body(request),
                        },
                    },
                    "Subject": {
                        "Charset": "UTF-8",
                        "Data": EmailService._get_subject(request),
                    },
                },
                Source=EmailService._get_sender(),
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response["Error"]["Message"])
        else:
            print("Email sent! Message ID:"),
            print(response["MessageId"])

    @staticmethod
    def _send_email_using_gmail_smpt(request):
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

    @staticmethod
    def send_email(request):
        # This is disabled since GMAIL does not allow SMPT anymore
        # EmailService._send_email_using_gmail_smpt(request)
        EmailService._send_email_using_amazon_ses(request)
