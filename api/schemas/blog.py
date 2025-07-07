from pydantic import BaseModel
from typing import Optional, TYPE_CHECKING
from datetime import date


if TYPE_CHECKING:
    from api.schemas.user import ShowUser

class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True  # ✅ This is correct
    }



class BlogRecord(BaseSchema):
    title: str
    body: str


class BlogCreate(BlogRecord):
    pass

class BlogUpdate(BaseSchema):
    title: Optional[str] = None
    body: Optional[str] = None

class Blogs(BaseSchema):
    id: int
    created_at: date
    

class ShowBlog(BaseSchema):
    title: str
    body: str
    author: list['ShowUser'] = []

from api.schemas.user import ShowUser
ShowBlog.model_rebuild()   