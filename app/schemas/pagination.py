from pydantic import BaseModel, Field

class PaginationParams(BaseModel):
    page: int = Field(
        default=1,
        ge=1
    )
    size: int = Field(
        default=20,
        le=100,
        ge=1
    )

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.size
    
    @property
    def limit(self) -> int:
        return self.size
    