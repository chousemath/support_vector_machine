from scipy.spatial import distance
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score
from typing import List
# from sklearn.neighbors import KNeighborsClassifier


def euclidean_distance(a: float, b: float) -> float:
    return distance.euclidean(a, b)


class ScrappyKnn():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train

    def predict(self, x_test) -> List[int]:
        predictions = []
        for row in x_test:
            predictions.append(self.closest(row))
        return predictions

    def closest(self, row):
        best_dist = euclidean_distance(row, self.x_train[0])
        best_indx = 0
        for i in range(1, len(self.x_train)):
            dist = euclidean_distance(row, self.x_train[i])
            if dist < best_dist:
                best_dist = dist
                best_indx = i
        return self.y_train[best_indx]


iris = datasets.load_iris()

x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.5)

clf = ScrappyKnn()

clf.fit(x_train, y_train)

predictions = clf.predict(x_test)

print(f'\nAccuracy score: {accuracy_score(y_test, predictions)}\n')
