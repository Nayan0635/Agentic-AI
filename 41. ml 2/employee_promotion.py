from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


#reading from csv file
df=pd.read_csv("./database/employee_promotion.csv")
# #Displaying all Data
# print(df)
#select input and output
X = df[["experience_years","performance_score","training_hours"]]
#Want to display all inputs.
# print(X)
y=df['promoted']

#Split into training Data and testing Data
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

#Create an Model of the DescisionTreeClassifier
model = DecisionTreeClassifier(
    max_depth=3, # Limits the tree to a maximum depth of 3 levels
    random_state=42
)

#Training the model.
model.fit(X_train,y_train)
print("Model Training has completed")

y_pred = model.predict(X_test)
#Predicted Result
# print("Predicted Result")
# print(y_pred)
# #Actual result
# print("Actual Result")
# print(y_test)

#Now calculating accuracy
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,classification_report
accuracy = accuracy_score(y_test,y_pred)
print("Model Accuracy :",accuracy)

#Now calculating precision
precision = precision_score(y_test,y_pred, pos_label="Yes",zero_division=0)
print("Model Precision :",precision)

#Now calculating recall
recall =recall_score(y_test,y_pred,pos_label="Yes",zero_division=0)
print("Model Recall :",recall)

f1score = f1_score(  y_test, y_pred, pos_label="Yes", zero_division=0)
print("Model F1 Score:",f1score)


clr_report = classification_report(y_test,y_pred)
print("Model Evaluation Metrics:")
print(clr_report)

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

plt.figure(figsize=(14, 7))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=[str(c) for c in model.classes_],
    filled=True,
    rounded=True
)

plt.savefig("./database/employee_promotion.png", dpi=300, bbox_inches="tight")
# plt.show()

print("Image saved successfully")

