import random
#lets implement a class for a classifiers
class BarebonesKNN():
    def fit(self, X_train, y_train):
        #pass the data in setter
        self.X_train = X_train
        self.y_train = y_train
        pass
    def predict(self, X_test):
        predictions = []
        #lets randomlly use a row
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions


from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target


#lets parttition the datsets
from sklearn.cross_validation import train_test_split
#calculate accuracy
from sklearn.metrics import accuracy_score
#partition the data into two sets one for training and one for testing
#X_train and y_train are the features and labels for training set
#X_test and y_test are the features and labels for the test set
#split the date in half
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

#use our out classifier
my_classifier = BarebonesKNN()
#train
my_classifier.fit(X_train, y_train)
#predit on our test cases
predictions = my_classifier.predict(X_test)
print str(accuracy_score(y_test, predictions)) + ' decision tree accuracy'
