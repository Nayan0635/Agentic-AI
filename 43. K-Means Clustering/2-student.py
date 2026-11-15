import os
os.environ["LOKY_MAX_CPU_COUNT"] = "0"

import pandas as pd
from sklearn.cluster import KMeans

from pathlib import Path
db_path = Path(__file__).parent / "data" / "student_clusters.csv"

df = pd.read_csv(db_path)

x = df[["Study_Hours","Attendance"]]

model = KMeans(n_clusters=5, random_state=42, n_init=10)

model.fit(x)

#internally designed groups or clusters
# print(model.labels_)

newStudent = [[float(input("Enter study hours :")), float(input("Enter attendance :"))]]
result = model.predict(newStudent)
print(f"New student belongs to Group : {result[0]}")
