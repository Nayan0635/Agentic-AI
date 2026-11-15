from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
import pandas as pd

from pathlib import Path
db_path = Path(__file__).parent / "data" / "car_price_prediction.csv"

#print(df)
df = pd.read_csv(db_path)

x = df[["car_age","mileage"]]
y = df['car_price']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

newCar= pd.DataFrame({
    "car_age":[int(input("Enter car age :"))],
    "mileage":[int(input("Enter mileage :"))],
})
result = model.predict(newCar)
print(round(result[0],2))