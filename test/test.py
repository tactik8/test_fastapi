# main.py
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{test_data}")
async def fn_test_data(test_data):
    return {"message": "Hello World"}

#uvicorn.run(app,host="0.0.0.0",port=8080)
