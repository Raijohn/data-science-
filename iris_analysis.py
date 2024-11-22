import pandas as pd
iris_df = pd.read_csv("iris.csv")
print(iris_df.head(5))
print(iris_df[["sepal_length","sepal_width","petal_length","petal_width"]].min(),iris_df[["sepal_length","sepal_width","petal_length","petal_width"]].mean(),iris_df[["sepal_length","sepal_width","petal_length","petal_width"]].max()) 
print(iris_df["species"].value_counts())
print(iris_df[iris_df["petal_length"]>iris_df["petal_length"].mean()],iris_df[iris_df["petal_width"]>iris_df["petal_width"].mean()])

print(iris_df.agg({"petal_length":["min","max"],"petal_width":["min","max"]}))

print(iris_df.groupby("species")[["sepal_length","sepal_width"]].mean())

iris_df["species"] = iris_df["species"].str.upper()
print(iris_df)

print(iris_df.groupby("species").median())

print("number of rows:",iris_df.shape[0],"number of colums",iris_df.shape[1])

print(iris_df[(iris_df["species"] != "SETOSA")])