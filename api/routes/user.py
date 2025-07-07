from fastapi import APIRouter, Depends
from api.schemas.user import UserCreate, UserUpdate, ShowUser
from sqlalchemy.orm import Session
import database
from api.crud.user import user_crud
from typing import List


user_router = APIRouter()


@user_router.post("/", status_code=201)
def create_user(request_data: UserCreate, db: Session = Depends(database.get_db)):
    return user_crud.create_user(request_data, db)

@user_router.put("/{user_id}", status_code=200)
def update_user(user_id: int, request_data: UserUpdate, db: Session = Depends(database.get_db)):
    return user_crud.update_user(user_id, request_data, db)

@user_router.get("/{user_id}", status_code=200, response_model=ShowUser)
def get_user_by_id(user_id: int, db: Session = Depends(database.get_db)):
    return user_crud.get_users_by_id(user_id, db)

@user_router.get("/", status_code=200, response_model=List[ShowUser])
def get_all_user(db: Session = Depends(database.get_db)):
    return user_crud.get_all_users(db)