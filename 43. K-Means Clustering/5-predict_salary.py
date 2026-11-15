from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
import pandas as pd

from pathlib import Path
db_path = Path(__file__).parent / "data" / "employee_salary.csv"

#print(df)
df = pd.read_csv(db_path)

x = df[["experience_years"]]
y = df['annual_salary_inr']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

model = LinearRegression()
model.fit(x_train,y_train)

emp= pd.DataFrame({
    "experience_years":[int(input("Enter experience years :"))]
})
result = model.predict(emp)
print(round(result[0],2))