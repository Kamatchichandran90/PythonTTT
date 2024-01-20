import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread("kitty.jpg")
print(type(img))
print(img.shape)
weights = np.array([0.3, 0.59, 0.11])
grayscale = img @ weights
mpimg.imsave("good-gray.jpg", grayscale, cmap="gray")
