import matplotlib.pyplot as plt
import pandas as pd
import sklearn
import sklearn.linear_model

data = pd.read_csv("prices.csv")
data["Cena"] = data["Cena"].str.replace(",00 zł", "")
data["Cena"] = data["Cena"].str.replace(" ", "").astype(int)


data["Powierzchnia"] = (
    data["Powierzchnia"]
    .str.replace(",", "")
    .str.pad(width=4, side="right", fillchar="0")
)
data["Powierzchnia"] = data["Powierzchnia"].astype(int)

powierzchnia_median = data["Powierzchnia"].median()
cena_median = data["Cena"].median()

print(powierzchnia_median, cena_median)
print(data.head())

X = data[["Powierzchnia"]]
y = data["Cena"]

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)
X_new = [[2678.5]]
print(model.predict(X_new))

# plot linear regression
plt.scatter(X, y, color="black")
plt.plot(X, model.predict(X), color="blue", linewidth=3)
plt.show()
