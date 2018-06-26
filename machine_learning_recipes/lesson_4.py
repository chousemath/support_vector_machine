from pprint import pprint
from sklearn import datasets
from sklearn import tree
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
# one way to think of a classifier is as a function => f(x) = y, x is the input, y is the output
x = iris.data
y = iris.target

# paritition the data into training and testing datasets
# test_size represents the fraction of the dataset to include in the split
# in this case, we designate half of the dataset for testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)


def predict(clf, x_train, y_train, x_test) -> float:
    trained_model = clf.fit(x_train, y_train)
    predictions = trained_model.predict(x_test)
    print(f'\nPREDICTION ACCURACY: {accuracy_score(y_test, predictions)}\n')


# initialize and train a classifier
clf = tree.DecisionTreeClassifier()
predict(clf, x_train, y_train, x_test)

clf_2 = KNeighborsClassifier()
predict(clf_2, x_train, y_train, x_test)
