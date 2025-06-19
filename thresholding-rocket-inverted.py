import skimage as sk
from utils import show_image


image = sk.data.cat()
grayscale = sk.color.rgb2gray(image)

threshold = 0.5 # 255 // 2
binary = grayscale <= threshold
print(grayscale)

show_image.show3(image, grayscale, binary, cmap='gray')