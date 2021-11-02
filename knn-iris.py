#import datasets
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

print(iris.feature_names)
print(iris.target) #0-setosa, 1-versicolor, 2-virginica

from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=100)

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics #evaluate func

#set model
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
scores = metrics.accuracy_score(y_test, y_pred)
print(scores)