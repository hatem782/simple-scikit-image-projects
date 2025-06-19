import skimage as sk
from utils import show_image

image = sk.data.rocket()
red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

show_image.show_histogram_with_image(image,red,green,blue)

