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
