from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
n_samples =2000
np.random.seed(0)
Data, labels = datasets.make_moons(n_samples, noise=0.10)
plt.scatter(Data[:, 0], Data[:, 1], c=labels, s=2, cmap='viridis')