import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

result = df[(df.index % 20 == 0) & (df.index != 0)][['Manufacturer', 'Model', 'Type']]

print(result)