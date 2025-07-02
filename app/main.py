from fastapi import FastAPI


app = FastAPI(title='Blog API')






@app.get("/")
def index():
    return {'message': 'Blog App is running'}