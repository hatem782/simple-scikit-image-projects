import matplotlib.pyplot as plt

def show(image, title='Image', camp_type='gray'):
    plt.imshow(image, cmap=camp_type)
    plt.title(title)
    plt.axis('off')
    plt.show()


def show3(img1, img2, img3, titles=('Red', 'Green', 'Blue'), cmap='gray'):
    plt.figure(figsize=(12, 4))  

    images = [img1, img2, img3]
    for i, img in enumerate(images):
        plt.subplot(1, 3, i + 1)
        plt.imshow(img, cmap=cmap)
        plt.title(titles[i])

    plt.tight_layout()
    plt.show()


def show_with_channels(original, red, green, blue):
    plt.figure(figsize=(10, 6))

    plt.subplot(2, 2, 1)
    plt.imshow(original)
    plt.title('Original')

    channel_images = [red, green, blue]
    titles = ['Red', 'Green', 'Blue']

    for i, (img, title) in enumerate(zip(channel_images, titles)):
        plt.subplot(2, 2, i + 2)
        plt.imshow(img, cmap='gray')
        plt.title(title)

    plt.tight_layout()
    plt.show()

def show_histogram_with_image(image, red, green, blue):
    plt.figure(figsize=(10, 6))

    # Show original image (top row)
    plt.subplot(2, 2, 1)
    plt.imshow(image)
    plt.title('Original Image')
    plt.axis('off')

    # Red channel histogram
    plt.subplot(2, 2, 2)
    plt.hist(red.ravel(), bins=256, color='red', alpha=0.8)
    plt.title('Red Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Count')

    # Green channel histogram
    plt.subplot(2, 2, 3)
    plt.hist(green.ravel(), bins=256, color='green', alpha=0.8)
    plt.title('Green Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Count')

    # Blue channel histogram
    plt.subplot(2, 2, 4)
    plt.hist(blue.ravel(), bins=256, color='blue', alpha=0.8)
    plt.title('Blue Histogram')
    plt.xlabel('Intensity')
    plt.ylabel('Count')

    plt.tight_layout()
    plt.show()