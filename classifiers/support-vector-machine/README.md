# Support Vector Machine demos
**Dr. Chris Empson, Infinity Works Ltd.**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

Twitter: [@monty_mcmont](https://twitter.com/monty_mcmont)

## Overview
These demos demonstrate binary and radial basis function classification using support vector machines.

### `svm_lemon_or_banana.py`
This binary classification demo demonstrates the simplest possible case of classification, where two data sets are linearly separable. The application generates two sets of data comprising two dimensions, pH (acidity) and length. One of the populations represents the properties of lemons, the other bananas. 

The Support Vector Machine selects the 'support vectors' on which it bases its decision boundary. These data points are highlighted in grey. No other data points are taken into account when the boundary is calculated. 

When the user clicks on the plot the model is queried and the resulting classification is displayed.

### `svm_rbf.py`
This demo demonstrates a slightly more complex case in which one dataset is distinct from another, surrounding data set. These datasets are not linearly separable in two dimensions, so we can't simply plot a straight line to separate them.

Instead the SVM classifier does something clever. It projects the data into an *n*-dimensional space, where *n* is the number of features that it finds in the data. A straight line in *n*-dimensional space can then be drawn between the two data sets. This line is then projected back into two dimensions, where it no longer appears straight!

As in the *lemon or banana* classification demo, the 'support vectors' upon which the model defines the decision boundary are highlighted in grey.

When the user clicks on the plot the model is queried and the resulting classification is displayed.


## Running the demos
You will need python3, numpy, scipy, scikit-learn and matplotlib to run these demos.

```pip3 install numpy && pip3 install scipy && pip3 install scikit-learn && pip3 install matplotlib```

To style the classifier plots in the intended manner copy the matplotlib-stylelib/iw.mplstyle to your matplotlib style library, e.g.:

```mkdir -p ~/.matplotlib-conf/stylelib/ && cp classifiers/support-vector-machine/matplotlib-stylelib/iw.mplstyle ~/.matplotlib/stylelib/```

The demos do not require any command-line arguments. They can be run directly, e.g.:

```python3 svm_lemon_or_banana.py```

## References, useful links and whatnot

http://scikit-learn.org/stable/modules/svm.html

https://mubaris.com/2017/10/14/svm-python/

https://stackoverflow.com/questions/23794277/extract-decision-boundary-with-scikit-learn-linear-svm
