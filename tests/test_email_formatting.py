from app.email_formatter import EmailFormatter
from app.schemas import MemberRequest, DonationRequest


class TestEmailFormatting:
    def test_formatting(self):
        result = EmailFormatter.format_email_for_request(
            MemberRequest(
                full_name="Test Name",
                birthdate="22/12/2020",
                email="Test Email",
                phone_number="Test Phone Number",
                already_a_member=True,
                health_worker=False,
                professional_experience="Test Professional Experience",
                years_of_experience=3,
                have_experience=True,
                first_time=False,
            )
        )
        assert (
            result == "Nombre: Test Name\n"
            "Fecha de nacimiento: 22/12/2020\n"
            "Email: Test Email\n"
            "Número de teléfono: Test Phone Number\n"
            "Ya es miembro: Sí\n"
            "Es sanitario: No\n"
            "Experiencia profesional: Test Professional Experience\n"
            "Tiene experiencia: Sí\n"
            "Primera vez en Humancoop: No\n"
        )

        result = EmailFormatter.format_email_for_request(
            DonationRequest(
                full_name="Test Name",
                nif="Test Nif",
                address="Test Address",
                city="Test City",
                province="Test Province",
                postcode="Test Postcode",
                email="Test Email",
                phone_number="Test Phone Number",
                account_number="Test Account Number",
                account_owner_name="Test Account Owner Name",
                amount="Test Amount",
            )
        )
        assert (
            result == "Nombre: Test Name\n"
            "NIF: Test Nif\n"
            "Dirección: Test Address\n"
            "Localidad: Test City\n"
            "Provincia: Test Province\n"
            "Código postal: Test Postcode\n"
            "Email: Test Email\n"
            "Número de teléfono: Test Phone Number\n"
            "Número de cuenta: Test Account Number\n"
            "Nombre del titular: Test Account Owner Name\n"
            "Cantidad: Test Amount €"
        )
