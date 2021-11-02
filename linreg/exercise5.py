import matplotlib.pyplot as plt
from sklearn import linear_model

reg = linear_model.LinearRegression()

x = [[0], [30], [10], [15], [5], [25], [35], [40], [45]]
y = [4, 1, 3, 2, 3, 1, 0, 1, 1]

reg.fit(x, y)

print(reg.predict([[0]]))

plt.scatter(x, y, color="black")
y_pred = reg.predict(x)
plt.plot(x, y_pred, color="blue", linewidth=3)
plt.show()