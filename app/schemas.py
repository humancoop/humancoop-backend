from pydantic import BaseModel, Field


class MemberRequest(BaseModel):
    full_name: str = Field(title="Volunteer name")
    birthdate: str = Field(title="Volunteer name")
    email: str = Field(title="Volunteer name")
    phone_number: str = Field(title="Volunteer name")
    already_a_member: bool = Field(title="Volunteer name")
    health_worker: bool = Field(title="Volunteer name")
    professional_experience: str = Field(title="Volunteer name")
    years_of_experience: int = Field(title="Volunteer name")
    have_experience: bool = Field(title="Volunteer name")
    first_time: bool = Field(title="Volunteer name")
    where_did_you_know: str = Field(title="Volunteer name")


class DonationRequest(BaseModel):
    full_name: str = Field(title="Volunteer name")
    nif: str = Field(title="Volunteer name")
    address: str = Field(title="Volunteer name")
    city: str = Field(title="Volunteer name")
    province: str = Field(title="Volunteer name")
    postcode: str = Field(title="Volunteer name")
    email: str = Field(title="Volunteer name")
    phone_number: str = Field(title="Volunteer name")
    account_number: str = Field(title="Volunteer name")
    account_owner_name: str = Field(title="Volunteer name")
    amount: str = Field(title="Volunteer name")
