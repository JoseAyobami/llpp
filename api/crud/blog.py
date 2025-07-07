from fastapi import HTTPException, Response
from api.schemas.blog import  BlogCreate,  BlogUpdate, ShowBlog
from sqlalchemy.orm import Session
from api.models.blog import Blog as BlogModel


class BlogCrud:

    @staticmethod
    def create_blog(request_data: BlogCreate, db: Session):
        blog = BlogModel(
            body = request_data.body,
            title = request_data.title,
            author_id = 1
        )

        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog
    
    @staticmethod
    def update_blog(blog_id: int, request_data: BlogUpdate, db: Session):
        blog_update = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if not blog_update:
            raise HTTPException(status_code=404, detail="Blog not found")
        db.query(BlogModel).filter(BlogModel.id == blog_id).update(request_data.model_dump())
        db.commit()
        return {'message': 'Blog updated'}
    
    @staticmethod
    def get_by_blog_id(blog_id: int, db: Session):
        blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if not blog:
            raise HTTPException(status_code=404, detail="Blog not found")
        return ShowBlog.model_validate(blog)
    
    @staticmethod
    def get_all_blogs(db: Session):
        all_blogs = db.query(BlogModel).all()
        reults = []
        for blog in all_blogs:
            show_blog = ShowBlog.model_validate(blog)
            reults.append(show_blog)
        return reults
    
    @staticmethod
    def delete_blog(blog_id: int, db: Session):
        blog_delete = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        if not blog_delete:
            raise HTTPException(status_code=404, detail="Blog not found")
        db.query(BlogModel).filter(BlogModel.id == blog_id).first()
        db.commit()
        return Response(status_code=204) 
         
    #{'message': 'Blog deleted successfully'}"""



blog_crud = BlogCrud()    