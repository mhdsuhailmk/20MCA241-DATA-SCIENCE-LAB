#!/usr/bin/env python
# coding: utf-8

# In[15]:


#importing dataset(remote)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

#loading dataset
iris = load_iris()
x = iris.data
y = iris.target

#splitting the dataset into test ,train
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)
c_knn = KNeighborsClassifier(n_neighbors=5)
c_knn.fit(x_train,y_train)
y_pred = c_knn.predict(x_test)


#to check accuracy of the model
print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))

sample = [[2,2,7,3]]
pred = c_knn.predict(sample)
pred_v = [iris.target_names[p] for p in pred]
print(pred_v)


# In[ ]:




