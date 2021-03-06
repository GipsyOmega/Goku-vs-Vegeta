# -*- coding: utf-8 -*-
"""Goku & Vegeta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L1hXHvTu2rgjgASGPLhlYGYes8u1Rx4_
"""

!unzip /content/dbz.zip

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline
import tensorflow as tf
import os
import cv2

print(len(os.listdir('/content/DB dataset/Training/goku')))
print(len(os.listdir('/content/DB dataset/Training/vegeta')))
print(len(os.listdir('/content/DB dataset/Testing/goku')))
print(len(os.listdir('/content/DB dataset/Testing/vegeta')))

from google.colab.patches import cv2_imshow
folder="/content/DB dataset/Training/goku"
i=0
for x in os.listdir(folder):
  path=os.path.join(folder,x)
  img=cv2.imread(path)
  cv2_imshow(img)
  print("          Goku Image {}".format(i+1))
  print()
  i+=1
  if i>3:
    break;

folder="/content/DB dataset/Training/vegeta"
i=0
for x in os.listdir(folder):
  path=os.path.join(folder,x)
  img=cv2.imread(path)
  cv2_imshow(img)
  print("         Vegeta Image {}".format(i+1))
  print()
  i+=1
  if i>3:
    break;

from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


model.compile(optimizer=RMSprop(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])

model.summary()

TRAINING_DIR = "/content/DB dataset/Training/"
train_datagen = ImageDataGenerator(rescale=1.0/255., 
                                   rotation_range=40,
                                   zoom_range=0.3,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   horizontal_flip=True,
                                   shear_range=0.2,
                                   fill_mode='nearest')
train_generator = train_datagen.flow_from_directory(TRAINING_DIR,
                                                    batch_size=50,
                                                    class_mode='binary',
                                                    target_size=(150, 150))

VALIDATION_DIR = "/content/DB dataset/Testing/"
validation_datagen = ImageDataGenerator(rescale=1.0/255.,
                                        rotation_range=40,
                                        zoom_range=0.3,
                                        width_shift_range=0.2,
                                        height_shift_range=0.2,
                                        horizontal_flip=True,
                                        shear_range=0.2,
                                        fill_mode='nearest')
validation_generator = validation_datagen.flow_from_directory(VALIDATION_DIR,
                                                              batch_size=50,
                                                              class_mode='binary',
                                                              target_size=(150, 150))

history = model.fit(train_generator, epochs=25, steps_per_epoch=5,
                    validation_data=validation_generator)

# Model has an accuracy of about 70%

from google.colab import files
from keras.preprocessing import image

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

classes
#This is lesser than 0.5, hence the model predicts the image to be Goku!!
#But it is Vegeta!
#Prediction is Wrong!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is greater than 0.5, the model predicts it to be VEGETA!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is greater than 0.5, the model predicts it to be VEGETA!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is greater than 0.5, the model predicts it to be VEGETA!
#The prediction is WRONG!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is greater than 0.5, the model predicts it to be VEGETA!
#The prediction is CORRECT!

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images, batch_size=10)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

print(x.shape)
print(images.shape)

uploaded = files.upload()

for y in uploaded.keys():
 
  # predicting images
  path = '/content/' + y
  img = image.load_img(path, target_size=(150, 150))
  x = image.img_to_array(img)
  x = x / 255
  x = np.expand_dims(x, axis=0)
  images = np.vstack([x])
  classes = model.predict(images)
  print(classes[0])
  print()
  if classes[0]<0.5:
    print(" This is Goku!")
  else:
    print(" This is Vegeta!")
print()
plt.imshow(img)

#Since the value of classes is less than 0.5, the model predicts it to be GOKU!
#The prediction is CORRECT!

#. Made by ARYAMAN RAO, STUDENT, UNGERGRAD FROM DELHI TECHNOLOGICAL UNIVERSITY, INDIA