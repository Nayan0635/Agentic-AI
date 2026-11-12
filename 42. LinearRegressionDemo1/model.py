#import LinearRegression Model.
from sklearn.linear_model import LinearRegression
#Splitting the training and testing Data
from sklearn.model_selection import train_test_split
#for reading from .csv file
import pandas as pd
#for saving the Model locally on HDD
import joblib #comes with scikit-learn we dont need to install it additionally.

df = pd.read_csv("./database/house_price_prediction.csv")
#Printing all Data from csv
#print(df)

#Input selections
X = df[['area_sqft','bedrooms']]
#print(X)
#Result
y = df['house_price_inr']
#print(y)
#Splitting into Training and Test Data.
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#Create the model here
model = LinearRegression()
#Here we are training the model.
model.fit(X_train,y_train)
joblib.dump(model,"./database/house_price_calc")
print("Model has been saved successfully")

