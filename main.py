from graph import create_image, image_to_nodes
from plot import plot_slice
import numpy as np

image = create_image(zeros=2)
print(np.asarray(np.gradient(image)).shape)
bin = np.where(image != 0, 1, 0)
print(bin.sum())

nodes = image_to_nodes(image)
print(len(nodes))
print(nodes[:5])

plot_slice(image, 8)