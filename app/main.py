from pydantic import BaseSettings
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from .schemas import MemberRequest, DonationRequest
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


origins = ["http://localhost:8080"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/new_member", status_code=HTTPStatus.OK)
def member(request: MemberRequest):
    logger.info(request.content)
    return Response(status_code=HTTPStatus.OK)


@app.post("/new_donation", status_code=HTTPStatus.OK)
def donation(request: DonationRequest):
    logger.info(request.content)
    return Response(status_code=HTTPStatus.OK)
