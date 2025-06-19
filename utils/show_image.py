import matplotlib.pyplot as plt

def show(image, title='Image', camp_type='gray'):
    plt.imshow(image, cmap=camp_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
