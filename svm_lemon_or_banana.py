from mldemos import svm
from sklearn.datasets import make_blobs
from time import sleep
import numpy as np

# Generate training dataset containing two linearly seperable centers
# containing 100 points each, with a spread of 2 standard deviations.
# Interesting random_states: 78 - linearly seperable, 7 - some overlap
training_data, centre_ids = make_blobs(
    n_samples=200,
    centers=2,
    random_state=82,
    cluster_std=1
)

# Offset and scale the data points to make them more fruit-like!
training_data = training_data + np.array([11, 8])
training_data = training_data * np.array([0.5, 1])

class_labels = ['Lemon', 'Banana']
axis_labels = ['pH', 'Length (cm)']

# Create linear SVM and display plot
plot = svm.BinarySvm(training_data, centre_ids, 'linear', 1.0, class_labels, axis_labels)
