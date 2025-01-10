import pandas as pd

data_pf = pd.read_csv("Data.csv")
print(data_pf.head(10))

#check for missing values
print(data_pf.isnull().sum())

#take care of missing values

#remove them
#data_pf.dropna(inplace=True)

#replace them
#manual
'''mean_Age = data_pf["Age"].mean()
mean_Salary = data_pf["Salary"].mean()
data_pf.loc[data_pf["Age"].isnull(),"Age"] = mean_Age
data_pf.loc[data_pf["Salary"].isnull(),"Salary"] = mean_Salary'''

#
from sklearn.impute import SimpleImputer
simpleimputer = SimpleImputer(missing_values=pd.NA,strategy="mean")
data_pf[["Age","Salary"]] = simpleimputer.fit_transform(data_pf[["Age","Salary"]])
print(data_pf.head(10))

#split into featurs and target
X = data_pf[["Country","Age","Salary"]]
y = data_pf["Purchased"]

print("fearured: ",X)
print("target: ",y)

#encoding catagorical data in featurs
x_dummies = pd.get_dummies(X,columns=["Country"],dtype=int)
print(x_dummies)
#encoding catagorical dat in target
#manual
#y.replace({"Yes":1,"No":0},inplace=True)

from sklearn.preprocessing import LabelEncoder

var = LabelEncoder()

y = var.fit_transform(y)

print(y)

#split into training and test set
from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest = train_test_split(x_dummies,y,train_size=0.8,random_state=42)

print("xtrain\n",xtrain,"\nxtest\n",xtest,"\nytrain\n",ytrain,"\nytest\n",ytest)
