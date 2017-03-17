from sklearn import treee
#feature contains the inputs to classifier
#scikit uses real-valued data
#1 denotes smooth 2 denotes bumpy
features = [[140, 1], [130 , 1], [150, 0], [170, 0]]
#these are the likely outputs we want from the classifier
#0 apple 1 orange
labels =[0, 0, 1, 1]

#train a classifer
#decision tree
#create a classifier
clf = tree.DecisionTreeClassifier()
#learning alogrithm
clf = clf.fit(features, labels) # fit fine patterns in data

print clf.predict([[110, 1], [160, 0]])
