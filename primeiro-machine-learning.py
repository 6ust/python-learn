%matplotlib inline
from sklearn.datasets import load_iris
from sklearn.model_selection import  train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as pyplot
import numpy as np


iris= load_iris()
iris.keys()

print(iris['DESCR'][:193] + '\n...')

iris['target_names'] #types o iris

iris['feature_names'] #types o iris

print(iris['data'].shape)
iris['data'][:10] # Contains the measurement of each flower

# an numpy array containing 0 to 2 values. Each one for flower type. 0 for Setosa, 1 for Versicolor, 2 for  Virginica 
iris['target']


# Train and test
X_train, X_test, Y_train, Y_test = train_test_split(iris['data'], iris['target'], random_state = 0)
print(X_train.shape)
print(X_test.shape)



fig, ax = pyplot.subplots(3, 3, figsize=(15,15))

for i in range(3):
	for j in range(3):
		ax[i,j].scatter(X_train[:,j], X_train[:, i + 1], c = Y_train, s=60)
		ax[i,j].set_xticks(())
		ax[i,j].set_yticks(())

		if i == 2:
			ax[i,j].set_xlabel(iris['feature_names'][j])
		if j == 0:
			ax[i,j].set_ylabel(iris['feature_names'][i + 1])
		if j >  i:
			ax[i,j].set_visible(False)


# Creating the model
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, Y_train)

# Testing model
X_new = np.array([[5, 2.9, 1, 0.2]])
X_new,shape

prediction = knn.predict(X_new)
prediction

iris['target_names'][prediction]

knn.score(X_test, Y_test)