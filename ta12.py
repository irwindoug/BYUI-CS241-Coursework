# Getting Started
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

data = pd.read_csv("weather_year.csv")

# Fun with Columns
data.columns = ["date", "max_temp", "mean_temp", "min_temp", "max_dew","mean_dew", "min_dew", "max_humidity", "mean_humidity", "min_humidity", "max_pressure", "mean_pressure", "min_pressure", "max_visibilty", "mean_visibility", "min_visibility", "max_wind", "mean_wind", "min_wind", "precipitation", "cloud_cover", "events", "wind_dir"]

data.mean_temp.hist()

# Bulk Operations with apply()
first_date = data.date.values[0]

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))

data.index = data.date

data = data.drop(["date"], axis=1)

# Handling Missing Values
empty = data.apply(lambda col: pd.isnull(col))

data.dropna(subset=["events"])

data.events = data.events.fillna("")

# Accessing Individual Rows
num_rain = 0
for idx, row in data.iterrows():
    if "Rain" in row["events"]:
        num_rain += 1

print("Days with rain: {0}".format(num_rain))
