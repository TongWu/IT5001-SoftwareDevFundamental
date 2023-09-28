import imageio
import matplotlib.pyplot as plt



def image_composition(filename1, filename2):
    # Load the foreground and background images
    foreground = imageio.imread(filename1)
    background = imageio.imread(filename2)

    # Iterate over the pixels
    for i in range(foreground.shape[0]):
        for j in range(foreground.shape[1]):
            r, g, b = foreground[i, j]
            if g > r and g > b and g > 110:  # Check for green criteria
                foreground[i, j] = background[i, j]

    # Save the resultant image
    imageio.imwrite('aveNUgerS.jpg', foreground)

    # Display the original images
    plt.figure(figsize=(10, 5))

    plt.subplot(2, 2, 1)
    plt.imshow(imageio.imread(filename1))
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(imageio.imread(filename2))
    plt.axis('off')

    plt.subplot(2, 1, 2)
    plt.imshow(foreground)
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    return

#Uncomment the following for your own testing

#image_composition('avengers green.jpg','background.jpg')


image_composition('avengers green triangle.jpg','background.jpg')


