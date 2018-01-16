from mldemos import svm
from sklearn.datasets import make_gaussian_quantiles

# Generate training dataset containing two classes, one inside the other,
# containing 100 points each, with a covariance of 3.
# Interesting random_states: 2 - 100% seperable
X, y = make_gaussian_quantiles(
    n_samples=200,
    n_features=2,
    n_classes=2,
    cov=3,
    random_state=2
)

# Create radial basis function SVM and display plot
svm.svm(X, y, 'rbf', 100)