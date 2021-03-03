
from __future__ import absolute_import, division, print_function, unicode_literals
from random import randint
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from PIL import Image, ImageOps

pd.options.display.max_rows = 10
pd.options.display.float_format = "{:.1f}".format

np.set_printoptions(linewidth = 200)

(x_train, y_train),(x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train_normalized = x_train / 255
x_test_normalized = x_test / 255

#saving images pre-augmentation
test_image_1 = Image.fromarray(x_train[0])
test_image_1 = test_image_1.convert("RGB")
test_image_1.save('/Users/wyattja1/Downloads/test_image_1.png',quality = 95)
test_image_2 = Image.fromarray(x_train[1000])
test_image_2 = test_image_2.convert("RGB")
test_image_2.save('/Users/wyattja1/Downloads/test_image_2.png',quality = 95)
test_image_3 = Image.fromarray(x_train[2000])
test_image_3 = test_image_3.convert("RGB")
test_image_3.save('/Users/wyattja1/Downloads/test_image_3.png',quality = 95)

def train_data_augmenter():
      i = 0
      if i <=59999:
          random_number = randint(1,3)
          i#if random_number = 1, no augmentation
          if random_number == 2:
                #function to flip image
                img = Image.fromarray(x_train[i])
                
                augmented_image = tf.keras.Sequential([
                  layers.experimental.preprocessing.RandomFlip("horizontal_and_vertical"),
                  ])
                #flip augmentation
                img = augmented_image(img)
                img = numpy.array(img)
                x_train[i] = img
          if random_number == 3:
                img = Image.fromarray(x_train[i])
                #function to rotate image
                augmented_image = tf.keras.Sequential([
                  layers.experimental.preprocessing.RandomRotation(0.2),
                  ])
                #rotate augmentation
                img = augmented_image(img)
                img = numpy.array(img)
                x_train[i] = img
          i = i + 1
train_data_augmenter()
  #saving the augmented version of test images
test_image_1 = Image.fromarray(x_train[0])
test_image_1 = test_image_1.convert("RGB")
test_image_1.save('/Users/wyattja1/Downloads/test_image_1_augmented.png',quality = 95)
test_image_2 = Image.fromarray(x_train[1000])
test_image_2 = test_image_2.convert("RGB")
test_image_2.save('/Users/wyattja1/Downloads/test_image_2_augmented.png',quality = 95)
test_image_3 = Image.fromarray(x_train[2000])
test_image_3 = test_image_3.convert("RGB")
test_image_3.save('/Users/wyattja1/Downloads/test_image_3_augmented.png',quality = 95)