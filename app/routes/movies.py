from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from app.backend.db_depends import get_db
from typing import List, Annotated, Dict
from app.schemas.schemas import CreateMovie, MovieOut, UpdateMovie
from sqlalchemy.ext.asyncio import AsyncSession
from app.crud import movies as crud_movies

router = APIRouter(prefix="/api/movies", tags=["movies"])


@router.get('/', response_model=Dict[str, List[MovieOut]])
async def get_all_movies(db: Annotated[AsyncSession, Depends(get_db)]):
    movies = await crud_movies.get_all_movies(db)
    return {"list": movies}


@router.get("/{movie_id}", response_model=Dict[str, MovieOut])
async def get_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    movie = await check_db_exceptions(crud_movies.get_movie, db, movie_id)
    return {"movie": movie}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movie(db: Annotated[AsyncSession, Depends(get_db)], movie: CreateMovie):
    await crud_movies.create_movie(db, movie)
    return {
        "status": "Movie created successfully",
        "transaction": "Successful"
    }


@router.patch("/{movie_id}")
async def update_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int, updates_movie: UpdateMovie):
    update_data = updates_movie.dict(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    updated_movie = await check_db_exceptions(crud_movies.update_movie, db, movie_id, update_data)
    return {"status": "Movie updated successfully", "movie": updated_movie}


@router.delete("/{movie_id}")
async def delete_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    await check_db_exceptions(crud_movies.delete_movie, db, movie_id)
    return {"status": status.HTTP_200_OK, "message": "Movie deleted successfully"}


async def check_db_exceptions(operation, *args, **kwargs):
    try:
        return await operation(*args, **kwargs)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Movie not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
