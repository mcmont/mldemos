from mldemos import svm
from sklearn.datasets import make_gaussian_quantiles

# Generate training dataset containing two classes, one inside the other,
# containing 100 points each, with a covariance of 3.
# random_state = 2 is 100% separable
X, y = make_gaussian_quantiles(
    n_samples=200,
    n_features=2,
    n_classes=2,
    cov=3,
    random_state=2
)

class_labels = ['In', 'Out']
axis_labels = ['X dimension', 'Y dimension']

# Create radial basis function SVM and display plot
svm.BinarySvm(X, y, 'rbf', 100, class_labels, axis_labels)
