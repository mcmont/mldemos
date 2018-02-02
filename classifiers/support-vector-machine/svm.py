import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


class BinarySvm:
    """
    Generate an interactive plot of the SVM training data, decision boundary
    and margins. Clicking in the plot displays the classification of the point.
    """
    aqua = '#00b2a9'
    light_blue = '#77eeff'
    classifier = None
    classifier_fit = None
    class_labels = None
    axis_labels = None

    def __init__(self, X, y, kernel_name, C, class_labels, axis_labels):

        available_kernels = ['linear', 'rbf']
        if kernel_name not in available_kernels:
            print('Invalid kernel type, choose one of %s' % (available_kernels))
            return

        if len(class_labels) != 2:
            print('Please supply 2 class labels')
            return
        self.class_labels = class_labels

        if len(axis_labels) != 2:
            print('Please supply 2 axis labels')
            return
        self.axis_labels = axis_labels

        # A large regularisation value C (~1000) tells our model that we do
        # not have that much faith in our data's distribution, so it should
        # only consider points close to line of separation.
        # A small value of C (0.001) includes more/all the observations, 
        # allowing the margins to be calculated using all the data in the 
        # area. The default is 1.0
        if C is None:
            C = 1.0

        # Get the name of the kernel initialisation function, and execute it.
        kernel_function = getattr(self, 'init_kernel_'+kernel_name)
        self.classifier = kernel_function(C)

        # Split the data into training and test sets.
        # The training data will be used to fit the model,
        # the validation data will be used to score it.
        X_train, X_validation, y_train, y_validation = train_test_split(X, y, test_size=0.3, shuffle=True)

        # Train the model
        self.classifier_fit = self.get_fit(X_train, y_train)
        # Classify the validation data
        print('%s percent of validation data points were correctly classified.' % (self.get_score(X_validation, y_validation)*100))
        self.draw_svm(X_train, y_train, kernel_name, C)

    def init_kernel_linear(self, C):
        """ Get a linear SVM kernel with regularisation parameter C. """
        return SVC(kernel='linear', C=C)

    def init_kernel_rbf(self, C):
        """
        Get a radial basis function kernel with regularisation parameter C.
        Auto gamma equals 1/n_features.
        https://en.wikipedia.org/wiki/Radial_basis_function_kernel
        """
        return SVC(kernel='rbf', C=C, gamma='auto')

    def get_fit(self, X, y):
        """ Get the classifier fit. """
        return self.classifier.fit(X, y)

    def get_score(self, X, y):
        """ Return the model fit score based on the test data"""
        return self.classifier.score(X, y)

    def draw_svm(self, X, y, kernel_name, C):
        """ Draw the plot using mPyPlot. """
        # Set the plot window size
        plt.rcParams["figure.figsize"] = (20, 10.5)
        # Apply Infinity Works styling
        style.use('iw')
        plt.title(self.class_labels[0]+' or '+self.class_labels[1]+'?')

        # Plot the training data points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap='autumn')
        axes = plt.gca()
        axes.set_xlabel(self.axis_labels[0])
        axes.set_ylabel(self.axis_labels[1])

        # Calculate the decision boundary and the margins.
        xlim = axes.get_xlim()
        ylim = axes.get_ylim()
        xx = np.linspace(xlim[0], xlim[1], 200)
        yy = np.linspace(ylim[0], ylim[1], 200)
        YY, XX = np.meshgrid(yy, xx)
        xy = np.vstack([XX.ravel(), YY.ravel()]).T
        Z = self.classifier.decision_function(xy).reshape(XX.shape)

        # Draw the decision boundary and the margins.
        axes.contour(XX, YY, Z, colors=self.aqua, levels=[-1, 0, 1],
                            alpha=0.5, linestyles=['--', '-', '--'])

        # Highlight the support vectors
        axes.scatter(self.classifier.support_vectors_[:, 0],
                    self.classifier.support_vectors_[:, 1],
                    s=200, linewidth=1, marker='o', alpha=0.2)
        
        # Register mouse button event handler
        fig = plt.gcf()
        fig.canvas.mpl_connect('button_press_event', self.handle_click)

        # Enter the display loop
        plt.show()

    def handle_click(self, event):
        """ Display a classified data point when the user clicks within the axes. """
        # Classify the new point
        class_index, = self.classifier.predict([(event.xdata, event.ydata)])
        print('Point at %.2f, %.2f belongs to class %s' % (event.xdata, event.ydata, self.class_labels[class_index]))
        # Plot the new point
        axes = plt.gca()
        axes.scatter(event.xdata, event.ydata, c=self.light_blue)
        plt.text(event.xdata-0.07, event.ydata+0.15, self.class_labels[class_index])
        # Redraw the plot
        plt.draw()
