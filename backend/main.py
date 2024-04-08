#main.py

from fastapi import FastAPI
from core.config import settings

# app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)
app = FastAPI()

@app.get("/")
def hello_api():
    return {"msg":"Hello FastAPI🚀"}

# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}