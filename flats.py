import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import sklearn.linear_model

df = pd.read_csv("flats.csv")
plt.scatter(df["area"], df["price"])
plt.xlabel("Area")
plt.ylabel("Price")

X = df[["area"]]
y = df["price"]

model = sklearn.linear_model.LinearRegression()
model.fit(X, y)

X_new = [[30]]

prediction = model.predict(X_new)
plt.plot(X, model.predict(X), color="red")

plt.show()
