import pandas as pd
import matplotlib.pyplot as plt
path = "/Users/zacharynemnijones/Desktop/Brooklyn_Bridge_Automated_Pedestrian_Counts_Demonstration_Project"
df = pd.read_csv(path)
print(df.head())
df['hour'] = pd.to_datetime(df['hour'])
df['day'] = df['hour'].dt.day_name()
df = df.sort_values(by='hour').reset_index(drop=True)
df['temperature'].fillna(method='ffill', inplace=True)
df['precipitation'].fillna(method='ffill', inplace=True)
df['weather_summary'].fillna(method='ffill', inplace=True)

plt.figure(figsize=(10, 5))
plt.plot(df['day'], df['Pedestrians'], color='blue')
plt.title('Pedestrian Counts Over Time')
plt.xlabel('Day')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
plt.show()
