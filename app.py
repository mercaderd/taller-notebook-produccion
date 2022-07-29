from fastapi import FastAPI
import bikesmodel
import datetime as dt

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello, World!"}

@app.post("/train_and_persist")
async def do_train_and_persist():
    bikesmodel.train_and_persist()
    return {"success": True}


@app.get("/predict")
async def do_predict(
    dteday: dt.date,
    hr: int,
    weathersit: str,
    temp: float,
    atemp: float,
    hum: float,
    windspeed: float,
):
    result = bikesmodel.predict(
        dteday,
        hr,
        weathersit,
        temp,
        atemp,
        hum,
        windspeed,
    )
    return {"number_cyclists": result}