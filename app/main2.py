from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from . import models 
from .database import engine
from . routers import users, posts, auth, vote

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router=posts.router)
app.include_router(router=users.router)
app.include_router(router=auth.router)
app.include_router(router=vote.router)

# Get Method
@app.get("/")
def root():
    return {"message": "Hello World we made some changes"}
