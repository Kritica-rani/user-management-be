from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api import users
from app import models, database

# Create tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the users routes
app.include_router(users.router, prefix="/users", tags=["users"])
