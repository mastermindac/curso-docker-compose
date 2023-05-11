from datetime import datetime, timedelta, timezone

import jwt
from flask import Response, make_response

from flasktodos.config import Config
from flasktodos.models import User, UserSchema


ACCESS_TOKEN_EXPIRE_DELTA = timedelta(minutes=15)
REFRESH_TOKEN_EXPIRE_DELTA = timedelta(days=3)


def issue_jwt(user: User, secret: str, expire_delta: timedelta) -> str:
    expires_at = datetime.now(tz=timezone.utc) + expire_delta

    payload = {
        "user": {"id": user.id},
        "exp": expires_at,
    }

    return jwt.encode(payload, secret)


def create_access_token(user: User) -> str:
    return issue_jwt(
        user=user,
        secret=Config.JWT_ACCESS_SECRET,
        expire_delta=ACCESS_TOKEN_EXPIRE_DELTA
    )


def create_refresh_token(user: User) -> str:
    return issue_jwt(
        user=user,
        secret=Config.JWT_REFRESH_SECRET,
        expire_delta=REFRESH_TOKEN_EXPIRE_DELTA
    )


def set_refresh_token_cookie(response: Response, token: str):
    response.set_cookie(
        key="rt",
        value=token,
        httponly=True,
        samesite="None",
        secure=True,
        path="/auth/token/refresh",
        expires=datetime.now(tz=timezone.utc) + REFRESH_TOKEN_EXPIRE_DELTA,
    )


def login_response(user: User) -> Response:
    response = make_response({
        "access_token": create_access_token(user),
        "user": UserSchema(exclude=["password"]).dump(user),
    })
    set_refresh_token_cookie(response, create_refresh_token(user))

    return response


def logout_response() -> Response:
    response = make_response()
    set_refresh_token_cookie(response, "")

    return response
