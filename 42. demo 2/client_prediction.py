import pandas as pd
import joblib

newCar= pd.DataFrame({
    'car_age':[5],
    'mileage':[50000]
})
model = joblib.load("./database/car_price_calc")
result = model.predict(newCar)
print(round(result[0],2))