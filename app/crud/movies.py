from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update
from app.models import Movies
from app.schemas.schemas import CreateMovie
from sqlalchemy.exc import NoResultFound


async def get_all_movies(db: AsyncSession):
    result = await db.execute(select(Movies))
    return result.scalars().all()


async def get_movie(db: AsyncSession, movie_id: int):
    movie = await db.get(Movies, movie_id)
    if not movie:
        raise NoResultFound("Movie not found")
    return movie


async def create_movie(db: AsyncSession, movie: CreateMovie):
    new_movie = Movies(
        id=movie.id,
        title=movie.title,
        year=movie.year,
        director=movie.director,
        length=movie.length,
        rating=movie.rating
    )
    db.add(new_movie)
    await db.commit()
    await db.refresh(new_movie)
    return new_movie


async def delete_movie(db: AsyncSession, movie_id: int):
    movie = await db.get(Movies, movie_id)
    if not movie:
        raise NoResultFound("Movie not found")
    await db.delete(movie)
    await db.commit()


async def update_movie(db: AsyncSession, movie_id: int, update_data: dict):
    result = await db.execute(select(Movies).where(Movies.id == movie_id))
    movie = result.scalar_one_or_none()
    if not movie:
        raise NoResultFound("Movie not found")
    await db.execute(update(Movies).where(Movies.id == movie_id).values(**update_data))
    await db.commit()
    return movie
