from .schemas import MemberRequest


class EmailFormatter:
    @staticmethod
    def format_email_for_request(request):
        if isinstance(request, MemberRequest):
            return (
                f"Nombre: {request.full_name}\n"
                f"Fecha de nacimiento: {request.birthdate}\n"
                f"NIF: {request.nif}\n"
                f"Dirección: {request.address}\n"
                f"Localidad: {request.city}\n"
                f"Provincia: {request.province}\n"
                f"Código postal: {request.postcode}\n"
                f"Email: {request.email}\n"
                f"Número de teléfono: {request.phone_number}\n"
                f"Otro número de teléfono: {request.secondary_phone_number}\n"
                f"Número de cuenta: {request.account_number}\n"
                f"Nombre del titular: {request.account_owner_name}\n"
                f"¿Dónde nos conociste?: {request.where_did_you_know}"
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
