import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from .internal import admin
from .routers import items, users

app = FastAPI()


load_dotenv()
HOST = os.environ.get("HOST") or "127.0.0.1"
PORT = int(str(os.environ.get("PORT"))) or 5173

app.include_router(users.router)
app.include_router(items.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={418: {"description": "I'm a teapot"}},
)


def main():
    uvicorn.run(app, host=HOST, port=PORT)


if __name__ == "__main__":
    main()
