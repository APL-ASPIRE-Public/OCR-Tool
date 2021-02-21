import numpy as np
from PIL import Image
import cv2
import os

IMG_DIR = '/Users/singhs2/Desktop/1096202_64x64.jpg'
for img in os.listdir(IMG_DIR):
    img_array = cv2.imread(os.path.join(IMG_DIR,img), cv2.IMREAD_GRAYSCALE)
    
    img_pil = Image.fromarray(img_array)
    img_28x28 = np.array(img_pil.resize(28,28))
    img_array = (img_28x28.flatten())
    
    print (img_array)
    