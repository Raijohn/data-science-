import pandas as pd
import matplotlib.pyplot as plt

covid_df = pd.read_csv("WHO-COVID-19-global-data.csv")

print(covid_df.info())

covid_df["DateReported"] = pd.to_datetime(covid_df["DateReported"])

print(covid_df.info())

print(covid_df.isnull().sum())

covid_df.drop(["Country_code"],inplace=True,axis=1)

print(covid_df.info())

grouped_daily_cases = covid_df.groupby("DateReported")
grouped_daily_cases2 = grouped_daily_cases.sum()

print(grouped_daily_cases2)

plt.plot(grouped_daily_cases2.index,grouped_daily_cases2["Cumulative_cases"])

plt.show()

plt.plot(grouped_daily_cases2.index,grouped_daily_cases2["New_cases"])

plt.show()

plt.plot(grouped_daily_cases2.index,grouped_daily_cases2["Cumulative_deaths"])

plt.show()

grouped_country = covid_df.groupby("Country")

grouped_country2 = grouped_country.get_group("Afghanistan")

print(grouped_country2)

plt.plot(grouped_country2["DateReported"],grouped_country2["Cumulative_cases"])

plt.show()

plt.plot(grouped_country2["DateReported"],grouped_country2["New_cases"])
plt.show()