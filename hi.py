# import the necessary packages
import sys

import cv2
import matplotlib.pyplot as plt
import numpy as np
import requests
from skimage.metrics import structural_similarity as ssim

print(sys.version)
print(sys.executable)

r = requests.get('https://cnn.com')
print(r.status_code)

name = input("Your name? ")
# name = "Jerry"
print("hi, ", name)
