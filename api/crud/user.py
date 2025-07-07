from fastapi import HTTPException
from api.schemas.user import UserCreate, UserUpdate, ShowUser
from sqlalchemy.orm import Session
from api.models.user import User as UserModel
from hashing import Hash


class UserCrud:

    @staticmethod
    def create_user(request_data: UserCreate, db: Session):
        existing_username = db.query(UserModel.username).filter(UserModel.username == request_data.username).first()
        if existing_username:
            raise HTTPException(status_code=400, detail='Username is already registered')
        
        existing_email = db.query(UserModel.email).filter(UserModel.email == request_data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail='Email is already existed')
        
        existing_passsword = db.query(UserModel.password).filter(UserModel.password == request_data.password).first()
        if existing_passsword:
            raise HTTPException(status_code=400, detail='Password already created')
        
        user = UserModel(
            username = request_data.username,
            email = request_data.email,
            password = Hash.encrypt(request_data.password),
            bio = request_data.bio
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    
    @staticmethod
    def update_user(user_id: int, request_data: UserUpdate, db: Session):
        user_update = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user_update:
            raise HTTPException(status_code=404, detail='User not found')
        db.query(UserModel).filter(UserModel.id == user_id).update(request_data.model_dump())
        db.commit()
        return {'message': 'User Credentials updated'}
    

    @staticmethod
    def get_users_by_id(user_id: int, db: Session):
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return ShowUser.model_validate(user)
    
    @staticmethod
    def get_all_users(db: Session):
        all_users = db.query(UserModel).all()
        result = []
        for user in all_users:
            show_user = ShowUser.model_validate(user)
            result.append(show_user)
        return result    




user_crud = UserCrud()