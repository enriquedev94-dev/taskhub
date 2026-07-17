from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=100,
    )
    description: str | None = Field(
        default=None,
        max_length=500,
    )
    completed: bool = Field(default=False)

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    # title, description, and completed are inherited from TaskBase
    model_config = ConfigDict(
        from_attributes=True,
    )