

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from keras.callbacks import CSVLogger

import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense
from keras import applications
from keras import optimizers

os.chdir('/home/cdsw/demo/models')


# dimensions of our images.
img_width, img_height = 150, 150

top_model_weights_path = 'bottleneck_fc_model2.h5'
train_data_dir = '/demo/data/train'
validation_data_dir = '/demo/data/test'



nb_train_samples = 200
nb_validation_samples = 200
epochs = 5
batch_size = 1

#csv_logger = CSVLogger(experiment_dir+'/classifier_training.log')


#os.makedirs(experiment_dir)

def save_bottlebeck_features():

	datagen = ImageDataGenerator(rescale=1. / 255)
	'''
	datagen = ImageDataGenerator(
		rotation_range=40,
		#width_shift_range=0.2,
		#height_shift_range=0.2,
		rescale=1./255,
		#shear_range=0.2,
	   # zoom_range=0.2,
		horizontal_flip=True,
		fill_mode='nearest')
	'''

	# build the VGG16 network
	model = applications.VGG16(include_top=False, weights='imagenet')
	
	generator = datagen.flow_from_directory(
		train_data_dir,
		target_size=(img_width, img_height),
		batch_size=batch_size,
		class_mode=None,
		shuffle=False)
	bottleneck_features_train = model.predict_generator(
		generator, nb_train_samples // batch_size)
	np.save(open('bottleneck_features_train_demo.npy', 'w'),
			bottleneck_features_train)
	
	print("Starting Create validation data>>>")

	generator = datagen.flow_from_directory(
		validation_data_dir,
		target_size=(img_width, img_height),
		batch_size=batch_size,
		class_mode=None,
		shuffle=False)
	bottleneck_features_validation = model.predict_generator(
		generator, nb_validation_samples // batch_size)
	np.save(open('bottleneck_features_validation_demo.npy', 'w'),
			bottleneck_features_validation)

	print("<<< Created Validation DATA >>>")
	

def train_top_model():
	train_data = np.load(open('bottleneck_features_train_demo.npy', 'rb'))
	train_labels = np.array(
		[0] * (100) + [1] * (100))

	validation_data = np.load(open('bottleneck_features_validation_demo.npy', 'rb'))
	validation_labels = np.array(
		[0] * (100) + [1] * (100))

	model = Sequential()
	model.add(Flatten(input_shape=train_data.shape[1:]))
	model.add(Dense(256, activation='relu'))
	model.add(Dropout(0.5))
	model.add(Dense(1, activation='sigmoid'))


	model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])


	history = model.fit(train_data, train_labels,
				  epochs=epochs,
				  #callbacks=[csv_logger],
				  batch_size=batch_size,
				  validation_data=(validation_data, validation_labels))

	model.save_weights(top_model_weights_path)

	print(history.history.keys())



#save_bottlebeck_features()
train_top_model()
