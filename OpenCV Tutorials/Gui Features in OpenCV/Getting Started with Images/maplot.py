import numpy as np
import cv2
import sys
from matplotlib import pyplot as plt

if len(sys.argv[1:])==1:
	img = cv2.imread(sys.argv[1],0)
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()