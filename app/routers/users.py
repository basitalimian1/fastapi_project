from .. import models , schemas, utils
from fastapi import status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/users",
                   tags=['Users'])

# Creating users
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user : schemas.UserCreate, db: Session = Depends(get_db)):

    # hash the password
    hashed_pwd = utils.hash(user.password)
    user.password = hashed_pwd

    new_user = models.User(**user.dict())  
    # Staging the post into database
    db.add(new_user)
    # Commiting the post
    db.commit()
    # Retrving that post
    db.refresh(new_user)

    return new_user

# get specific user

@router.get("/{id}",response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with {id} does not exist")
    return user
