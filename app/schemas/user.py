from pydantic import BaseModel, ConfigDict, EmailStr, Field

class UserBase(BaseModel):
    email: EmailStr
    name: str = Field(
        min_length=2,
        max_length=100,
    )

class UserCreate(UserBase):
    password: str = Field(
        min_length=8,
        max_length=100,
    )

class UserResponse(UserBase):
    id: int
    # email and name are inherited from UserBase
    model_config = ConfigDict(
        from_attributes=True,
    )