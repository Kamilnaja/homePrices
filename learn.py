import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.linear_model

df = pd.read_csv("prices.csv")
print(df.size)
df["Cena"] = df["Cena"].str.replace(",00 zł", "").str.replace(" ", "").astype(int)
df["Powierzchnia"] = (df["Powierzchnia"].str.replace(",", ".")).astype(float)

powierzchnia_median = df["Powierzchnia"].median()
cena_median = df["Cena"].median()

X = df[["Powierzchnia"]]
y = df["Cena"]

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)
X_new = [[26.5]]
print(model.predict(X_new))

plt.scatter(X, y, color="black")
# plt.plot(X, model.predict(X), color="blue", linewidth=3)
plt.show()
