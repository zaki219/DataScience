import pandas as pd
import matplotlib.pyplot as plt
path = "/Users/zacharynemnijones/Desktop/Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project"
df = pd.read_csv(path)
print(df.head())
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df = df.sort_values(by='hour_beginning')
df.reset_index(drop=True, inplace=True)

df['temperature'] = df['temperature'].ffill()
df['precipitation'] = df['precipitation'].ffill()
df['weather_summary'] = df['weather_summary'].ffill()

