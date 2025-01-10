import pandas as pd

iris_df = pd.read_csv("iris.csv")

print(iris_df.head())

print(iris_df.isnull().sum())

x = iris_df[["sepal_length","sepal_width","petal_length","petal_width"]]
y = iris_df["species"]

print("featured",x)
print("target",y)

from sklearn.preprocessing import LabelEncoder

var = LabelEncoder() 

y = var.fit_transform(y)

print(y)

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x,y,train_size=0.8,random_state=560)

print(xtrain.shape)
print(xtest.shape)
print(ytrain.shape)
print(ytest.shape)

from sklearn.tree import DecisionTreeClassifier

desision = DecisionTreeClassifier()
desision.fit(xtrain,ytrain)
prediction = desision.predict(xtest)

print(prediction)
print(ytest)

from sklearn import metrics

print(metrics.accuracy_score(ytest,prediction))