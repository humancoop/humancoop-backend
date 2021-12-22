from .test_base import client
from mock import patch


class TestApp:
    def test_new_member(self, client):
        response = client.post(
            "/new_member",
            json={
                "full_name": "Test",
                "birthdate": "Test",
                "nif": "Test",
                "address": "Test",
                "city": "Test",
                "province": "Test",
                "postcode": "Test",
                "email": "Test",
                "phone_number": "Test",
                "secondary_phone_number": "Test",
                "account_number": "Test",
                "account_owner_name": "Test",
                "amount": "Test",
                "period": "Test",
                "where_did_you_know": "Test",
            },
        )
        assert response.status_code == 200

    def test_new_donation(self, client):
        response = client.post(
            "/new_donation",
            json={
                "full_name": "Test",
                "birthdate": "Test",
                "nif": "Test",
                "address": "Test",
                "city": "Test",
                "province": "Test",
                "postcode": "Test",
                "email": "Test",
                "phone_number": "Test",
                "secondary_phone_number": "Test",
                "account_number": "Test",
                "account_owner_name": "Test",
                "amount": "Test",
                "where_did_you_know": "Test",
            },
        )
        assert response.status_code == 200
