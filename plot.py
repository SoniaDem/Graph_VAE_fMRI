import matplotlib.pyplot as plt
import numpy as np


def plot_slice(image,
               slices=1):
    """
    Function that plots the slices through z of an image where the image is stored as a numpy array
    :param image: A 3D image
    :type image: numpy array
    :param slices: number of slices
    :type slices: positive int
    :return:
    """

    slices = slices if 0 < slices <= image.shape[2] else image.shape[2]

    slice_id = np.int32(np.floor(np.linspace(0, image.shape[2]-1, slices)))

    plt.figure(figsize=(slices*4, 4))
    for i in range(slices):
        plt.subplot(1, slices, i+1)
        plt.imshow(image[:, :, slice_id[i]], cmap='Greys_r')
        plt.axis('equal')
        plt.axis('off')
        plt.title(f'slice {slice_id[i]}')

    plt.show()
