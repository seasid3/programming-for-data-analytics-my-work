# This code will investiage the relationship between windspeed and month
# Lab 1 - Week 7
# Author: Orla Woods

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("https://cli.fusio.net/cli/climate_data/webdata/mly4935.csv", skiprows=19)
# print(df.head(3))

# Investiage correlation between mean temperature and month
corrtemp = df["month"].corr(df["meant"])
print(f"Correlation between month and mean temperature: {corrtemp}")

# Clean windspeed data
cleandf = df[["month", "wdsp"]]

# Drop rows with missing windspeed values
cleandf['wdsp'] = cleandf.loc[:,('wdsp')].replace(' ', np.nan)
cleandf.dropna(inplace=True)

# save cleaned data to new csv
cleandf.to_csv("cleaned_winddata.csv", index=False)

# Convert windspeed to float
cleandf['wdsp'] = cleandf['wdsp'].astype(float)

# Analysis
corrwind = cleandf["month"].corr(cleandf["wdsp"])
print(f"Correlation between month and windspeed: {corrwind}")

# Regression (no relationship found above)
sns.set_style
# sns.scatterplot
sns.lmplot(x="month", y="wdsp", order=3, data=cleandf)
plt.title("Regression of Windspeed by Month")   
plt.xlabel("Month")
plt.ylabel("Windspeed (tenths of m/s)")     
plt.show()