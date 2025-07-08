from pydantic import BaseModel, EmailStr
from typing import Optional, List, TYPE_CHECKING


if TYPE_CHECKING:
    from api.schemas.blog import BlogRecord


class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True  
    }


class UserRecord(BaseSchema):
    username: str
    email: EmailStr
    password: str
    bio: str


class UserCreate(UserRecord):
    pass


class UserUpdate(BaseSchema):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None


class User(BaseSchema):
    username: str
    password: str


class Users(UserRecord):
    id: int
    is_active: bool = True



class ShowUser(BaseSchema):
    username: str
    email: EmailStr
    blogs: List['BlogRecord'] = []
    
    
    
from api.schemas.blog import BlogRecord
ShowUser.model_rebuild()
