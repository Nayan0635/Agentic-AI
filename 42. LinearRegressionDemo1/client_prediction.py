import pandas as pd
import joblib

newHouse= pd.DataFrame({
    'area_sqft':[1200],
    'bedrooms':[4]

})
model = joblib.load("./database/house_price_calc")
result = model.predict(newHouse)
print(round(result[0],2))