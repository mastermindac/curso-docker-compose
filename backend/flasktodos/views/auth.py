import jwt
from flask import Blueprint, abort, request
from werkzeug.security import check_password_hash, generate_password_hash

from flasktodos.auth.tokens import login_response, logout_response
from flasktodos.config import Config
from flasktodos.database import db
from flasktodos.models import User, UserSchema


blueprint = Blueprint("auth", __name__)


@blueprint.post("/register")
def register():
    user = UserSchema().load(request.json, transient=True)
    if User.query.filter_by(email=user.email).first() is not None:
        return {"message": "Email already exists."}, 400

    user.password = generate_password_hash(user.password)
    db.session.add(user)
    db.session.commit()

    return login_response(user)


@blueprint.post("/login")
def login():
    credentials = UserSchema().load(
        data=request.json,
        transient=True,
        partial=("name",)
    )

    user = User.query.filter_by(email=credentials.email).first()

    if user is None:
        abort(401)

    if not check_password_hash(user.password, credentials.password):
        abort(401)

    return login_response(user)


@blueprint.post("/logout")
def logout():
    return logout_response()


@blueprint.post("/token/refresh")
def refresh_token():
    token = request.cookies.get("rt", None)

    if token is None:
        abort(401)

    try:
        payload = jwt.decode(
            jwt=token,
            key=Config.JWT_REFRESH_SECRET,
            algorithms=["HS256"]
        )
    except (jwt.DecodeError, jwt.ExpiredSignatureError) as e:
        abort(401)

    user = User.query.filter_by(id=payload["user"]["id"]).first()
    
    if user is None:
        abort(401)

    return login_response(user)
