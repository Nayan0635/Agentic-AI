from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.requests import Request
import pandas as pd
import joblib


app=FastAPI()
#Backend Cors Free.
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
    return {"message":"welcome to HousePrice Calculator"}

@app.post("/calculate")
async def hourse_price_calculate(request:Request):
    data:dict = await request.json()
    square_feet= int(data.get("square_feet"))
    bedrooms   = int(data.get("bedrooms"))
    newHouse= pd.DataFrame({
    'area_sqft':[square_feet],
    'bedrooms':[bedrooms]

})
    model = joblib.load("./database/house_price_calc")
    result = model.predict(newHouse)
    #print(round(result[0],2))
    return {
        "newPrice":round(result[0],2),
        "bedrooms":bedrooms,
        "square_feet":square_feet
    }    
