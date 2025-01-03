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