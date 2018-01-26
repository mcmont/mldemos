from mldemos import svm
from sklearn.datasets import make_blobs
from time import sleep

# Generate training dataset containing two linearly seperable centers
# containing 100 points each, with a spread of 2 standard deviations.
# Interesting random_states: 78 - linearly seperable, 7 - some overlap
training_data, centre_ids = make_blobs(
    n_samples=200,
    centers=2,
    random_state=78,
    cluster_std=2
)

class_labels = ['Class 1', 'Class 2']
axis_labels = ['X dimension', 'Y dimension']

# Create linear SVM and display plot
plot = svm.BinarySvm(training_data, centre_ids, 'linear', 1.0, class_labels, axis_labels)
