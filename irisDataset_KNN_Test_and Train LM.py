from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data)

print(iris.data.shape)

print(iris.target.shape)

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 1)

x = iris.data
y = iris.target

knn.fit(x,y)

print(knn.predict([[4.6, 3.1, 1.5, 0.2] ] ) )

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.4, random_state = 42)

print(x_test.shape)


knn.fit(x_train, y_train)

predictions = knn.predict(x_test)

print(predictions)

from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)