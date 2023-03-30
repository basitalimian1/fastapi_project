from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
from pydantic import conint

class PostBase(BaseModel):
    title: str
    content: str
    published: bool


class CreatePost(PostBase):
    pass

class UserCreate(BaseModel):
    email :EmailStr
    password: str

class UserOut(BaseModel):
    id :int
    email: str
    create_at : datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True 

class Post(PostBase):
    id : int
    create_at : datetime
    owner_id : int
    owner : UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token : str
    token_type : str

    class Config:
        orm_mode = True 

class TokenData(BaseModel):
    id: Optional[str] = None

class Vote(BaseModel):
    post_id : int
    dir: conint(ge=0,le=1)