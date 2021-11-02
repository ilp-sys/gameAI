import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

x = [[1930], [1940], [1950], [1965], [1972], [1982], [1992], [2010], [2016]]
y = [59, 62, 70, 69, 71, 74, 75, 76, 78]

reg.fit(x, y)

print(reg.predict([[1962]]))

plt.scatter(x, y, color="black")
y_pred = reg.predict(x)
plt.plot(x, y_pred, color="blue", linewidth=3)
plt.show()