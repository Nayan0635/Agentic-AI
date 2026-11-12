from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
import pandas as pd
import joblib

app = FastAPI()

# Backend CORS Free.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return {"message": "Welcome to Car Price Calculator"}


@app.post("/calculate")
async def car_price_calculate(request: Request):
    data: dict = await request.json()

    car_age = int(data.get("car_age"))
    mileage = int(data.get("mileage"))

    newCar = pd.DataFrame({
        'car_age': [car_age],
        'mileage': [mileage]
    })

    model = joblib.load("./car_price_calc")
    result = model.predict(newCar)

    return {
        "newPrice": round(result[0], 2),
        "car_age": car_age,
        "mileage": mileage
    }

# python -m uvicorn api:app --reload --port 3000
# {
#     "car_age": 5,
#     "mileage": 50000
# }
