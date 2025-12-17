
from fastapi import FastAPI
from routers.books import router as books_router
from routers.users import router as users_router
from db import engine, Base

app = FastAPI()
app.include_router(books_router)
app.include_router(users_router)
Base.metadata.create_all(bind=engine)




