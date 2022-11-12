from .schemas import MemberRequest, SocioRequest


class EmailFormatter:
    @staticmethod
    def _format_bool(value):
        if value:
            return "Sí"
        return "No"

    @staticmethod
    def format_email_for_request(request):
        if isinstance(request, MemberRequest):
            return (
                f"Nombre: {request.full_name}\n"
                f"Fecha de nacimiento: {request.birthdate}\n"
                f"Email: {request.email}\n"
                f"Número de teléfono: {request.phone_number}\n"
                f"Ya es miembro: {EmailFormatter._format_bool(request.already_a_member)}\n"
                f"Es sanitario: {EmailFormatter._format_bool(request.health_worker)}\n"
                f"Experiencia profesional: {request.professional_experience}\n"
                f"Años de experiencia: {request.years_of_experience}\n"
                f"Tiene experiencia en voluntariado: {EmailFormatter._format_bool(request.have_experience)}\n"
                f"Primera vez en Humancoop: {EmailFormatter._format_bool(request.first_time)}\n"
                f"Dónde nos conoció?: {request.where_did_you_know}\n"
            )
        elif isinstance(request, SocioRequest):
            return (
                f"Nombre: {request.full_name}\n"
                f"NIF: {request.nif}\n"
                f"Dirección: {request.address}\n"
                f"Localidad: {request.city}\n"
                f"Provincia: {request.province}\n"
                f"Código postal: {request.postcode}\n"
                f"Email: {request.email}\n"
                f"Número de teléfono: {request.phone_number}\n"
                f"Número de cuenta: {request.account_number}\n"
                f"Nombre del titular: {request.account_owner_name}\n"
            )
        return (
            f"Nombre: {request.full_name}\n"
            f"NIF: {request.nif}\n"
            f"Dirección: {request.address}\n"
            f"Localidad: {request.city}\n"
            f"Provincia: {request.province}\n"
            f"Código postal: {request.postcode}\n"
            f"Email: {request.email}\n"
            f"Número de teléfono: {request.phone_number}\n"
            f"Número de cuenta: {request.account_number}\n"
            f"Nombre del titular: {request.account_owner_name}\n"
            f"Cantidad: {request.amount} €"
        )
