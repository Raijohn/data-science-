import pandas as pd
import matplotlib.pyplot as plt

covid_df = pd.read_csv("covid_data.csv")

print(covid_df.info())
print(covid_df.head())

#removing unnesisery colums

#setting axis to 1 is the same as setting collum to = the list
covid_df.drop(["Unnamed: 0","OBJECTID","Admin2","FIPS","Combined_Key","Last_Update"],inplace=True,axis=1)

print(covid_df.info())
print(covid_df.head())

print(covid_df.isnull().sum())
covid_df["Province_State"].fillna(" ",inplace=True)
print(covid_df.isnull().sum())

print(covid_df["Country_Region"].value_counts())

grouped_country = covid_df.groupby("Country_Region")
grouped_country2 = grouped_country.sum() 
grouped_country3 = grouped_country2.sort_values(by=["Confirmed"],ascending=False)

grouped_country4 = grouped_country2.sort_values(by=["Recovered"],ascending=False)

grouped_countr5 = grouped_country2.sort_values(by=["Deaths"],ascending=False)

top_10_confirmed = grouped_country3.head(10)

plt.figure(figsize =(14,12))
plt.bar(top_10_confirmed.index,top_10_confirmed["Confirmed"])
plt.show()

Us = grouped_country.get_group("US")
Us2 = Us.sort_values(by=["Confirmed"],ascending=False)

top_5_US = Us2.head(5)

print(top_5_US)

plt.scatter(top_5_US["Province_State"],top_5_US["Confirmed"],s=top_5_US["Confirmed"]/top_5_US["Confirmed"].min()*20)
plt.show()

top_10_recovery = grouped_country4.head(10)

plt.figure(figsize=(10,8))
plt.bar(top_10_recovery.index,top_10_recovery["Recovered"])
plt.show()

top_10_death = grouped_countr5.head(10)

plt.figure(figsize=(10,8))
plt.bar(top_10_death.index,top_10_death["Deaths"])
plt.show()