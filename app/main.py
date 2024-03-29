from pydantic import BaseSettings
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from .schemas import MemberRequest, DonationRequest, SocioRequest
from .email import EmailService
from http import HTTPStatus
import logging
import sys

app = FastAPI()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    ENVIRONMENT: str

    class Config:
        env_file = ".env"
        case_sensitive = True


origins = [
    "http://localhost:3000",
    "https://onghumancoop.org",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/new_member", status_code=HTTPStatus.OK)
def member(request: MemberRequest):
    logger.info(request)
    EmailService.send_email(request, "main")
    return Response(status_code=HTTPStatus.OK)


@app.post("/new_donation", status_code=HTTPStatus.OK)
def donation(request: DonationRequest):
    logger.info(request)
    EmailService.send_email(request, "accounting")
    return Response(status_code=HTTPStatus.OK)


@app.post("/new_socio", status_code=HTTPStatus.OK)
def socio(request: SocioRequest):
    logger.info(request)
    EmailService.send_email(request, "accounting")
    return Response(status_code=HTTPStatus.OK)
