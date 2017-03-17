#Import Data Set
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
#print iris.feature_names
#print iris.target_names
#import classifier
from sklearn import tree

#remove examples to test classifier after training
test_idx = [0, 50, 100]
#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
#Train a classifier to identify flower
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)
#Predict label for new flower
print 'expected answers'
print test_target
print clf.predict(test_data)
#visualize
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(clf,
                        out_file=dot_data,
                        feature_names=iris.feature_names,
                        class_names=iris.target_names,
                        filled=True,
                        rounded=True,
                        impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf('iris.pdf')
