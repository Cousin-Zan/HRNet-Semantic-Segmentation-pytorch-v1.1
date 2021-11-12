#!/usr/bin/env python
# coding: utf-8

# In[106]:


import tensorflow as tf
import numpy as np
import cv2 as cv
from glob import glob
import matplotlib.pyplot as plt


# In[107]:


labels = glob('./satellite images/labels/*.png')


# In[108]:


def read_png(path):
    img = tf.io.read_file(path)
    img = tf.image.decode_png(img, channels=3)
    return img


# In[109]:


def color2annotation(image):
    
    image /= 255
    image = 4 * image[:, :, 0] + 2 * image[:, :, 1] + image[:, :, 2]

    cat_image = np.zeros((512,512), dtype=np.uint8)
    cat_image[image == 3] = 0  # (Cyan: 011) Urban land
    cat_image[image == 6] = 1  # (Yellow: 110) Agriculture land
    cat_image[image == 5] = 2  # (Purple: 101) Rangeland
    cat_image[image == 2] = 3  # (Green: 010) Forest land
    cat_image[image == 1] = 4  # (Blue: 001) Water
    cat_image[image == 7] = 5  # (White: 111) Barren land
    cat_image[image == 0] = 6  # (Black: 000) Unknown

    return cat_image


# In[112]:


from tqdm import tqdm


# In[113]:


for i in tqdm(range(len(labels))):
    lbl = read_png(labels[i])
    mask = color2annotation(lbl)
    path = './mask/'
    name = labels[i].split('\\')[-1]
    filename = path + name
    output = tf.image.encode_png(mask[...,tf.newaxis])
    # 保存
    with tf.io.gfile.GFile(filename, 'wb') as file:
        file.write(output.numpy())


# In[94]:





# In[96]:




