from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

x,y=load_iris(return_x_y=True)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)
gnb=GaussianNB()
y_pred=gnb.fit(x_train,y_train).predict(x_test)
print(y_pred)
x_new=[[4,4,3,3]]
y_new=gnb.fit(x_train,y_train).predict(x_new)
print("predicted output for [[4,4,3,3]]:",y_new)
print("Naive bayes score               :",gnb.score(x_test,y_test))
