from pydantic import BaseModel, Field
from datetime import time


class CreateMovie(BaseModel):
    title: str = Field(max_length=100)
    year: int = Field(ge=1900, le=2100)
    director: str = Field(max_length=100)
    length: time = Field(example="02:30:00")
    rating: int = Field(ge=0, le=10)


class MovieOut(BaseModel):
    id: int
    title: str
    year: int
    director: str
    length: time
    rating: int


class UpdateMovie(BaseModel):
    title: str | None = None
    year: int | None = None
    director: str | None = None
    length: time | None = Field(example="02:30:00")
    rating: int | None = None
