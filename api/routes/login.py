from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from api.authentication.login import Login
from sqlalchemy.orm import Session
import database
from api.models.user import User as UserModel
from hashing import Hash 
from api.authentication.token import create_access_token


login_route = APIRouter()

@login_route.post("/", status_code=201)
def create_login(request_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(UserModel).filter(UserModel.email == request_data.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    
    if not Hash.verify(user.password, request_data.password):
        raise HTTPException(status_code=404, detail="Invalid Password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

    