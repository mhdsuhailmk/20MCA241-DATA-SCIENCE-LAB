 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

mnistDB = keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnistDB.load_data()


print("Shape of x_train:",x_train.shape)
print("Shape of x_test:",x_test.shape)
print("Shape of y_train:",y_train.shape)
print("Shape of y_test:",y_test.shape)

plt.imshow(x_train[33],cmap='binary')

x_train = x_train.reshape((60000,28,28,1))
x_test = x_test.reshape((10000,28,28,1))
x_train = x_train.astype('float32')/255
x_test = x_test.astype('float32')/255

print("Shape of x_train:",x_train.shape)
print("Shape of x_test:",x_test.shape)

cnnModel_MNIST = keras.models.Sequential()
cnnModel_MNIST.add(keras.layers.Conv2D(32,(3,3),activation="relu",input_shape=x_train.

shape[1:]))

cnnModel_MNIST.add(keras.layers.Conv2D(32,(3,3),activation="relu"))
cnnModel_MNIST.add(keras.layers.MaxPooling2D((2,2)))
