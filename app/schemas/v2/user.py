
from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserResponseV2(BaseModel):
    # id, first_name, last_name, and email are inherited from UserBaseV2
    id: int
    first_name: str
    last_name: str
    email: EmailStr