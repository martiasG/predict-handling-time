import numpy as np
import pandas as pd 
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import keras as k
from keras import layers
from keras.layers import Input, Dense, Activation, BatchNormalization, Dropout
from keras.models import Model, Sequential
from keras.utils import to_categorical
from keras.callbacks import TensorBoard

def load_model():
	model = Sequential()
	model.add(Dense(2048, input_dim=4, activation='relu'))
	model.add(Dense(1024, activation='relu'))
	model.add(Dense(512, activation='relu'))
	model.add(Dense(256, activation='relu'))
	model.add(Dense(128, activation='relu'))
	model.add(Dense(64, activation='relu'))
	model.add(Dense(32, activation='relu'))
	model.add(Dense(16, activation='relu'))
	model.add(Dense(8, activation='relu'))
	model.add(Dense(4, activation='relu'))
	model.add(Dense(1, activation='relu'))

	model.load_weights('params_model_300_no_norm.h5')
	# model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

	return model

model = load_model()