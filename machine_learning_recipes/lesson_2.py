# import dataset
import numpy as np
from pprint import pprint
from sklearn import tree
from sklearn.datasets import load_iris

iris = load_iris()

# Print out some metadata for the dataset
print('\nFEATURE NAMES:\n')
pprint(iris.feature_names)
print('\nTARGET NAMES\n')
TARGET_NAMES = list(iris.target_names)
pprint(TARGET_NAMES)

# Example of the actual data
print('\nFIRST ROW:\n')
pprint(iris.data[0])
pprint(TARGET_NAMES[iris.target[0]])

# split up the data and set some of it aside for testing purposes

# remove one example of each type of flower
test_idx = [0, 50, 100]
# training data: remove three entries from each of the data sets
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)
# testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# create a classifier
clf = tree.DecisionTreeClassifier()
# train a classifier
clf.fit(train_data, train_target)

# predict label for a new flower
predictions = clf.predict(test_data)
pprint(list(zip(test_target, predictions)))

# visualize the tree
