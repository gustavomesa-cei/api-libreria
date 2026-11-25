from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],      # Or ["*"] to allow all origins
        allow_credentials=True,     # Allow cookies and auth headers
        allow_methods=["*"],        # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],        # Allow all request headers
    )