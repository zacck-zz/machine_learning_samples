from scipy.spatial import distance
#use euc algorithm to return distance between objects
def euc(a,b):
    return distance.euclidean(a,b)

#lets implement a class for a classifiers
class BarebonesKNN():
    def fit(self, X_train, y_train):
        #pass the data in setter
        self.X_train = X_train
        self.y_train = y_train
        pass
    def predict(self, X_test):
        predictions = []
        #we iterate through test data
        for row in X_test:
            #find the closest element of a row
            label = self.closest(row)
            #label  the row
            predictions.append(label)
        return predictions
    #lets classify the data by getting the closest one
    def closest(self, row):
        #find shortest distance between the test data and a train data point
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        #walk through training data look for closer matches to our row
        for i in range (1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


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
