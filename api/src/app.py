from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def index():
    return {"text": "Hello"}

@app.get('/items/{name}')
async def get_items(name):
    return {"name": name}