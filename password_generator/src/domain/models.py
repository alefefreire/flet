from pydantic import BaseModel, Field, validator


class Password(BaseModel):
    value: str = Field(..., min_length=1)

    @validator("value")
    def value_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError("Password cannot be empty")
        return v
