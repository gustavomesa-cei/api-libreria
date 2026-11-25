import jwt
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

PUBLIC_PATHS = {"/", "/users/login", "/users/register", "/docs", "/openapi.json"}

class JWTAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if request.method == "OPTIONS" or request.url.path in PUBLIC_PATHS:
            return await call_next(request)

        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return JSONResponse(
                status_code=401,
                content={"detail": "Token faltante o formato inválido"},
            )

        token = auth_header.split(" ")[1]

        try:
            payload = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
            request.state.user = payload
        except jwt.ExpiredSignatureError:
            return JSONResponse(
                status_code=401, content={"detail": "El token ha expirado"}
            )
        except jwt.InvalidTokenError:
            return JSONResponse(
                status_code=401, content={"detail": "Token inválido"}
            )

        return await call_next(request)