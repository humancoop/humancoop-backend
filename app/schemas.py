from pydantic import BaseModel, Field


class MemberRequest(BaseModel):
    full_name: str = Field(title="Volunteer name")
    birthdate: str = Field(title="Volunteer name")
    nif: str = Field(title="Volunteer name")
    address: str = Field(title="Volunteer name")
    city: str = Field(title="Volunteer name")
    province: str = Field(title="Volunteer name")
    postcode: str = Field(title="Volunteer name")
    email: str = Field(title="Volunteer name")
    phone_number: str = Field(title="Volunteer name")
    secondary_phone_number: str = Field(title="Volunteer name")
    account_number: str = Field(title="Volunteer name")
    account_owner_name: str = Field(title="Volunteer name")
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
    secondary_phone_number: str = Field(title="Volunteer name")
    account_number: str = Field(title="Volunteer name")
    account_owner_name: str = Field(title="Volunteer name")
    amount: str = Field(title="Volunteer name")
