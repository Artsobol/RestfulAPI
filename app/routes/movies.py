from fastapi import APIRouter, Depends, status, HTTPException
from app.backend.db_depends import get_db
from typing import List, Annotated, Dict
from app.models import Movies
from sqlalchemy import insert, select
from app.schemas import CreateMovie, MovieOut
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/movies", tags=["movies"])


@router.get('/', response_model=Dict[str, List[MovieOut]])
async def get_all_movies(db: Annotated[AsyncSession, Depends(get_db)]):
    result = await db.execute(select(Movies))
    movie = result.scalars().all()
    return {"list": movie}


@router.get("/{movie_id}", response_model=Dict[str, MovieOut])
async def get_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    movie = await db.get(Movies, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"movie": movie}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movie(db: Annotated[AsyncSession, Depends(get_db)], create_movie: CreateMovie):
    await db.execute(
        insert(Movies).values(
            title=create_movie.title,
            year=create_movie.year,
            director=create_movie.director,
            length=create_movie.length,
            rating=create_movie.rating
        )
    )
    await db.commit()
    return {
        "status": "Movie created successfully",
        "transaction": "Successful"
    }


@router.delete("/{movie_id}")
async def delete_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    try:
        movie = db.get(Movies, movie_id)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        await db.delete(movie)
        await db.commit()
        return {"status": status.HTTP_202_ACCEPTED, "message": "Movie deleted successfully"}
    except Exception as e:
        return {"status": status.HTTP_500_INTERNAL_SERVER_ERROR, "reason": str(e)}
