import jwt
from flask import abort, g, request

from flasktodos.config import Config
from flasktodos.models.user import User


def auth():
    if request.method == "OPTIONS":
        return None

    authorization = request.headers.get("Authorization", "Invalid")
    if not authorization.startswith("Bearer "):
        abort(401)
    
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, Config.JWT_ACCESS_SECRET, algorithms=["HS256"])
    except (jwt.DecodeError, jwt.ExpiredSignatureError) as e:
        abort(401)

    g.user = User.query.get(payload["user"]["id"])
