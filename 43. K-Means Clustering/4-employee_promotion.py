import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


from pathlib import Path
db_path = Path(__file__).parent / "data" / "employee_promotion.csv"
df = pd.read_csv(db_path)

x = df.iloc[:, : -1]
y = df.iloc[: , -1]

x_train,x_test,y_train,y_test = train_test_split(x, y, train_size = 0.8, random_state = 42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

newEmployee= pd.DataFrame({
    "experience_years":[int(input("Enter experience years :"))],
    "performance_score":[int(input("Enter performance score :"))],
    "training_hours":[int(input("Enter training hours :"))]
})

result = model.predict(newEmployee)
print(f'New employee promoted? : {result[0]}')
