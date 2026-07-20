import jwt
from datetime import datetime, timedelta, timezone

class TokenService:

    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
    
    def create_access_token(self, user_id: str) -> str:
        payload = {
            "sub": str(user_id),
            "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
            "iat": datetime.now(timezone.utc)
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def verify_access_token(self, token: str) -> dict:
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

