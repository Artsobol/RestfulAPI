from typing import List, Annotated, Dict

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound, IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db_depends import get_db
from app.crud import movies as crud_movies
from app.schemas.schemas import MovieRequest, MovieOut, UpdateMovie

router = APIRouter(prefix="/api/movies", tags=["movies"])


@router.get('/', response_model=Dict[str, List[MovieOut]], status_code=status.HTTP_200_OK)
async def get_all_movies(db: Annotated[AsyncSession, Depends(get_db)]):
    movies = await crud_movies.get_all_movies(db)
    return {"list": movies}


@router.get("/{movie_id}", response_model=Dict[str, MovieOut], status_code=status.HTTP_200_OK)
async def get_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    movie = await check_db_exceptions(crud_movies.get_movie, db, movie_id)
    return {"movie": movie}


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_movie(db: Annotated[AsyncSession, Depends(get_db)], movie: MovieRequest):
    new_movie = await check_db_exceptions(crud_movies.create_movie, db, movie.movie)
    return {"movie": new_movie}


@router.patch("/{movie_id}")
async def update_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int, updates_movie: UpdateMovie):
    update_data = updates_movie.dict(exclude_none=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No data provided for update")

    updated_movie = await check_db_exceptions(crud_movies.update_movie, db, movie_id, update_data)
    return {"movie": updated_movie}


@router.delete("/{movie_id}", status_code=status.HTTP_202_ACCEPTED)
async def delete_movie(db: Annotated[AsyncSession, Depends(get_db)], movie_id: int):
    await check_db_exceptions(crud_movies.delete_movie, db, movie_id)
    return {"status": status.HTTP_202_ACCEPTED}


async def check_db_exceptions(operation, *args, **kwargs):
    try:
        return await operation(*args, **kwargs)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Movie not found")
    except IntegrityError:
        raise HTTPException(status_code=500, detail={"status": 500, "reason":"The ID is already occupied."})
    except Exception as e:
        raise HTTPException(status_code=500, detail={"status": 500, "reason": str(e)})
