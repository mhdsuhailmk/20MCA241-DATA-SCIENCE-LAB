 #DATASET IMPORTING...
from sklearn.datasets import load_iris
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#DATASET LOADING..
iris = load_iris()
x = iris.data
y = iris.target

#SPLITTING....
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)


#FITTING....
cls = DecisionTreeClassifier()
cls = cls.fit(x_train,y_train)
y_pred = cls.predict(x_test)

#ACCURACY CHECKING...
acc = metrics.accuracy_score(y_test,y_pred)


#VISUALIZATION....
plt.figure(figsize=(15,15))
tree.plot_tree(cls,fontsize=10,filled=True,rounded=True,class_names=iris.target_names,feature_names=iris.feature_names)
plt.show()






