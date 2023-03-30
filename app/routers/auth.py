from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from .. import database, models , schemas, utils, oauth2


router = APIRouter(tags=['Authentication'])

@router.post('/login', response_model=schemas.Token)
def login(user_credential: OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(database.get_db)):

    # Retriving details of user from database
    user = db.query(models.User).filter(models.User.email == user_credential.username).first()

    # checking if email is correct or not
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Invilid Credentials!")
    
    # Checking if password is correct or not
    if not utils.verify(plain_pwd=user_credential.password,hashed_pwd= user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, 
                            detail="Invilid Credentials!")
    
    # Create token
    access_token = oauth2.create_access_token(data= {"user_id": user.id})
    # retrun token

    return {"access_token":access_token,
            "token_type": "bearer"}
