import pandas as pd
import matplotlib.pyplot as plt

adult_income_df = pd.read_csv("adult_income.csv",sep=", ")

print(adult_income_df.info())
print(adult_income_df.head())

adult_income_df.drop(["fnlwgt","educational-num","capital-gain","capital-loss"],inplace=True,axis=1)

print(adult_income_df.info())
print(adult_income_df.head())

print(adult_income_df.isnull().sum())
for colum in adult_income_df.columns:
    print(adult_income_df[colum].value_counts())

adult_income_df.replace({"?","unknown"},inplace=True)
adult_income_df["income"].replace({">50K":1,"<=50K":0},inplace=True)

ages = adult_income_df[["age","income"]].groupby("age")
ages2 = ages.sum()

plt.bar(ages2.index,ages2["income"])
plt.show()

genders = adult_income_df[["gender","income"]].groupby("gender")
genders2 = genders.sum()


plt.bar(genders2.index,genders2["income"])
plt.show()