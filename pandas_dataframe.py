import pandas as pd
info = {"Name":["bob","jeff","jerry"],"Age":[10,20,30]}
info_df = pd.DataFrame(info)
print(info_df)
print(type(info_df))
#read a csv file
titanic_df = pd.read_csv("titanic.csv")
print(titanic_df)
#show rows fro the top
print(titanic_df.head(20))
#show rows from the bottom
print(titanic_df.tail(20))
#find number of rows and collums
print(titanic_df.shape)
#retrive single collum
print(titanic_df["Name"])
print(titanic_df["Age"].min())
#summery
print(titanic_df.info())
#statisticle summery
print(titanic_df.describe())
#retrive multiple
print(titanic_df[["Name","Age","Sex"]])
#filtering the records
print(titanic_df[titanic_df["Age"]>18])
print(titanic_df[(titanic_df["Pclass"]==1) & (titanic_df["Age"]<18)])
print(titanic_df[(titanic_df["Sex"] == "female") | (titanic_df["Pclass"] == 2)])
#index based slicing
print(titanic_df.iloc[0:400,0:4])
#conditinal slicing
print(titanic_df.loc[titanic_df["Sex"]=="female",["Pclass","Name","Age"]])
#getting colum names
print(titanic_df.columns)
#add new colum
titanic_df["Discount"] = titanic_df["Fare"] / 2
print(titanic_df.head(10))
#save and create new file
titanic_df.to_csv("titanic2.csv")
#changeing values
print(titanic_df.loc[0:3,"Name"])# = ["joe","bob","jeff"]
print(titanic_df.head(5))
#grouping data
grouped_collum = titanic_df.groupby("Pclass")
print(grouped_collum.max())
grouped_collum = titanic_df.groupby(["Pclass","Sex"])
print(grouped_collum.count())
#aggregated functions
Age = titanic_df[["Age","Fare"]]
print(Age.mean())
print(titanic_df.agg({"Age":["min","max"],"Fare":"mean"}))
#sorting
print(titanic_df.sort_values(by="Age"))
#renaming colums
titanic_df.rename(columns={"Pclass":"PassengerClass"},inplace=True)
print(titanic_df.columns)
#replace valus
titanic_df["Sex"].replace({"female":"F","male":"M"},inplace=True)
print(titanic_df.head(20))
#preforming string operations
print(titanic_df["Name"].str.lower())
print(titanic_df["Name"].str.split().str.get(-1))
titanic_df["LastName"] = titanic_df["Name"].str.split().str.get(-1)
print(titanic_df.head(10))

#Find the mean fare of passengers wrt sex and pclass like (Male 1st Class Passenger ). Do this for all possible combinations - Total 6 combinations.
print(titanic_df[["PassengerClass","Sex","Fare"]].groupby(["PassengerClass","Sex"]).mean())
