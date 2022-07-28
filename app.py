from fastapi import FastAPI
import bikesmodel

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, World!"}

@app.post("/train_and_persist")
async def do_train_and_persist():
    bikesmodel.train_and_persist()
    return {"success": True}


@app.post("/predict")
async def do_predict():
    ...