import numpy as np
import cv2
from matplotlib import pyplot as plt
img = cv2.imread('a.png',1)
#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
plt.imshow(img,interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show
#cv2.imwrite('rj.png',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
