import uvicorn
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.routes import movies

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]
    field_name = first_error['loc'][-1]
    error_message = first_error['msg']
    return JSONResponse(
        status_code=500,
        content={
            "status": 500,
            "reason": f"Field '{field_name}' {error_message}"
        }
    )


app.include_router(movies.router)

if __name__ == '__main__':
    uvicorn.run(app)
