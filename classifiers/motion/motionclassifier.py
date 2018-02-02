import collections
import csv
import numpy
from sklearn.neighbors import KDTree


class MotionClassifier(object):
    """ Class to load training data and find the nearest neighbours. """
    model = None
    training_data = numpy.empty(6)
    training_data_classes = numpy.empty(1)
    k = 5

    def __init__(self, k=5):
        self.k = k
        self.load_training_data()
        self.train_model()

    def load_training_data(self):
        """ Load the training data and class names from the data file. """
        with open('training_data.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                # Load all but the last column into the training_data array
                self.training_data = numpy.vstack((self.training_data, row[0:len(row)-1]))
                # Load the values in the last column into the training_data_classes array
                self.training_data_classes = numpy.vstack((self.training_data_classes, row[-1].strip()))

    def train_model(self):
        self.model = KDTree(self.training_data)

    def classify(self, movement_data):
        stats = numpy.fromstring(movement_data, sep=',')
        # print(stats)
        distances, nearest_neighbour_indices = self.model.query([stats], self.k)
        # print(distances, nearest_neighbour_indices)
        # Get the class labels of the k nearest neighbours
        nearest_labels = [self.training_data_classes[c][0] for c in nearest_neighbour_indices[0]]
        # print(nearest_labels)
        print(collections.Counter(nearest_labels).most_common(1)[0][0])