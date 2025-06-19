import skimage as sk
from utils import show_image

image = sk.data.colorwheel()
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

show_image.show_with_channels(image,red,green,blue)

