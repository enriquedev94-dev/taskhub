from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"
class TaskBase(BaseModel):
    title: str = Field(
        min_length=2,
        max_length=255,
    )
    description: str | None = Field(
        default=None,
        max_length=500,
    )
    status: TaskStatus = TaskStatus.TODO

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    project_id: int
    # title, description, and completed are inherited from TaskBase
    model_config = ConfigDict(
        from_attributes=True,
    )