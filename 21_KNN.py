#This excersize is to pick the best value of K

#Create a loop to apply KNN with values ranging from 1 to 25. 
#Test the performance of each K value and present the ones that best suits out dataset.

#could've used a list for k values but will use a dictonary instead b/c its easier to  generate a chart this way
from sklearn.neighbors import KNeighborsClassifier


k_value = {}
k = 1

from sklearn import metrics
performance = metrics.accuracy_score(y_test, predictions)
print(performance)

while (k <= 25):
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(x_train, ytrain)
    pedictions = knn.predict(x_test)
    performance = metrics.accuracy_score(y_test,predictions)
    kvalue(k) = round(performance, 4)
    k+=1
print(k_values)

import matplotlib.pyplot as plt
%matplotlib inline

plt.plot(list(k_values.keys()),list(k_values.values()))
plt.xlabel("Value of K")
plt.ylabel = ("Performance")
plt.show()


