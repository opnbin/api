import os
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    secret = os.environ.get("OPNBIN_SECRET")
    if not secret:
        raise HTTPException(status_code=500, detail="server misconfigured")
    if credentials.credentials != secret:
        raise HTTPException(status_code=401, detail="invalid token")
    return credentials.credentials
