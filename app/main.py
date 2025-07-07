from fastapi import FastAPI
from api import models
from database import engine
from api.routes.user import user_router
from api.routes.blog import blog_router
from api.routes.login import login_route


app = FastAPI(title='Blog API')
app.include_router(user_router, prefix='/user', tags=['users'])
app.include_router(blog_router, prefix='/blog', tags=['blogs'])
app.include_router(login_route, prefix='/login', tags=['login'])



models.Base.metadata.create_all(bind=engine)


@app.get("/")
def index():
    return {'message': 'Blog App is running'}