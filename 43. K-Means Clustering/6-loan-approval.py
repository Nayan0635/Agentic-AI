import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

from pathlib import Path
db_path = Path(__file__).parent / "data" / "take_loan.csv"
df = pd.read_csv(db_path)

x = df.drop(columns=["Loan_ID", "Applicant", "Loan_Approved"])
y = df["Loan_Approved"]

categorical_columns = [
    "Employment_Type",
    "Education",
    "Property_Area"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)
    ],
    remainder="passthrough"
)

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", DecisionTreeClassifier(max_depth=3, random_state=42))
])

x_train,x_test,y_train,y_test = train_test_split(x, y, train_size = 0.8, random_state = 42)

model.fit(x_train,y_train)

y_pred = model.predict(x_test)

person = pd.DataFrame({
    "Applicant_Income": [int(input("Enter applicant income: "))],
    "Loan_Amount": [int(input("Enter loan amount: "))],
    "Loan_Term_Months": [int(input("Enter loan term in months: "))],
    "Credit_Score": [int(input("Enter credit score: "))],
    "Employment_Type": [input("Enter employment type: ")],
    "Education": [input("Enter education: ")],
    "Dependents": [int(input("Enter number of dependents: "))],
    "Property_Area": [input("Enter property area: ")],
    "Existing_Debt": [int(input("Enter existing debt: "))]
})

result = model.predict(person)
print(f'Loan approved? : {result[0]}')

# "LN0001","Aarav Sharma - 0001","25919","63007","48","337","Self-Employed","High School","2","Semiurban","8190","No"
