import numpy as np


def create_image(x=16,
                 y=16,
                 z=16,
                 zeros=90):
    """
    (Joe's bad simulation function).
    This creates a 3D numpy array to represent a noisy image.
    :param x: the x dimension. (default :obj:`16`)
    :type x: positive int
    :param y: the y dimension. (default :obj:`16`)
    :type y: positive int
    :param z: the z dimension. (default :obj:`16`)
    :type z: positive int
    :param zeros: removes set amount of noise. (default :obj:`90`)
    :type zeros: positive int
    :return:
    """

    zeros = zeros if 0 < zeros <= 100 else zeros * 100

    image3d = np.zeros(shape=(x, y, z))
    for i in range(z):
        image2d = np.random.ranf(size=(x, y))

        rand_x = np.random.randint(low=0, high=x, size=(int(zeros*x),))
        rand_y = np.random.randint(low=0, high=y, size=(int(zeros*y),))
        for xi, yi in zip(rand_x, rand_y):
            image2d[xi, yi] = 0

        image3d[:, :, i] = image2d

    return image3d


def image_to_nodes(image):
    """
    This function takes a 3D image and converts each non-zero voxel to a node.
    :param image: an image stored as a 3D numpy array
    :type image: np.array
    :return:
    """

    image_grad = np.asarray(np.gradient(image))

    x, y, z = image.shape
    features = []
    indexer = 0
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if image[i, j, k] != 0:
                    features.append([indexer,
                                     image[i, j, k],
                                     image_grad[0, i, j, k],
                                     image_grad[1, i, j, k],
                                     image_grad[2, i, j, k]]
                                    )
                    indexer += 1

    return np.asarray(features)

