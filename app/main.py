import uvicorn
from fastapi import FastAPI
from app.routes import movies

app = FastAPI()

app.include_router(movies.router)

if __name__ == '__main__':
    uvicorn.run(app)