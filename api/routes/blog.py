from fastapi import APIRouter, Depends
from api.schemas.blog import  BlogCreate,  BlogUpdate, ShowBlog
from sqlalchemy.orm import Session
import database
from api.crud.blog import blog_crud
from typing import List
from api.schemas.user import User
import oauth2



blog_router = APIRouter()

@blog_router.post("/", status_code=201)
def create_blog(request_data: BlogCreate, db: Session = Depends(database.get_db)):
    return blog_crud.create_blog(request_data, db)

@blog_router.put("/{blog_id}", status_code=200)
def update_blog(blog_id: int, request_data: BlogUpdate, db: Session = Depends(database.get_db)):
    return blog_crud.update_blog(blog_id, request_data, db)

@blog_router.get("/{blog_id}", status_code=200, response_model=ShowBlog)
def get_blog_by_id(blog_id: int, db: Session=Depends(database.get_db)):
    return blog_crud.get_by_blog_id(blog_id, db)

@blog_router.get("/", status_code=200, response_model=List[ShowBlog])
def get_all_blogs(db: Session = Depends(database.get_db), get_current_user: User = Depends(oauth2.get_current_user)):
    return blog_crud.get_all_blogs(db)

@blog_router.delete("/{blog_id}", status_code=200)
def delete_blog(blog_id: int, db: Session= Depends(database.get_db)):
    return blog_crud.delete_blog(blog_id, db)