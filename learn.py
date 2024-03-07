import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/Users/kamilnaja/projects/ml/homePrices/prices.csv')
data['Cena'] = data['Cena'].str.replace(
    ',00 zł', '')
data['Cena'] = data['Cena'].str.replace(' ', '').astype(int)


data['Powierzchnia'] = data['Powierzchnia'].str.replace(
    ',', '').astype(int)

# pad 0 to right, if length is less than 4 for Powierzchnia
data['Powierzchnia'] = data['Powierzchnia'].astype(str).str.pad(
    width=4, side='right', fillchar='0')

# sort by Powierzchnia
data.sort_values(by='Powierzchnia', inplace=True)
print(data.head())
plt.scatter(data['Powierzchnia'], data['Cena'], color='red', marker='+')
plt.xticks(rotation=90)
plt.show()
