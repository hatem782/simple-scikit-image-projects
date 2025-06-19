import skimage as sk
from utils import show_image

image = sk.data.rocket()
grayscale = sk.color.rgb2gray(image)

# 3rd param is the color map, it can be : https://matplotlib.org/stable/tutorials/colors/colormaps.html
show_image.show(grayscale,"Grayscale",'gray')