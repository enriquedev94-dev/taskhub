from pydantic import BaseModel, EmailStr, Field, ConfigDict

class ProjectBase(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=100,
    )
    description: str | None = Field(
        default=None,
        max_length=500,
    )

class ProjectCreate(ProjectBase):
    pass

class ProjectResponse(ProjectBase):
    id: int
    # name and description are inherited from ProjectBase
    model_config = ConfigDict(
        from_attributes=True,
    )