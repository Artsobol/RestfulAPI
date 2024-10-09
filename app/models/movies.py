from datetime import time

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.backend.db import Base


class Movies(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    director: Mapped[str] = mapped_column(String(100), nullable=False)
    length: Mapped[time] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
