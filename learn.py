import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.linear_model

data = pd.read_csv('/Users/kamilnaja/projects/ml/homePrices/prices.csv')
data['Cena'] = data['Cena'].str.replace(
    ',00 zł', '')
data['Cena'] = data['Cena'].str.replace(' ', '').astype(int)


data['Powierzchnia'] = data['Powierzchnia'].str.replace(
    ',', '').str.pad(
    width=4, side='right', fillchar='0')
data['Powierzchnia'] = data['Powierzchnia'].astype(int)

print(data.head())

data.plot(kind='scatter', y='Powierzchnia', x='Cena')
plt.show()

X = data[['Powierzchnia']]
y = data['Cena']

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)
X_new = [[3000]]
print(model.predict(X_new))
