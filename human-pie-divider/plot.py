import argparse
from collections import defaultdict
import csv
import pprint
import sys
from typing import Dict, List

from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def _parse_args(args=sys.argv[1:]) -> argparse.Namespace:
    """Parse the command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", help="The full path to the CSV file containing responses", type=str, required=True)
    parser.add_argument("--groups", help="The number of groups", type=str, required=True)
    return parser.parse_args(args)


def _load_responses(csv_location: str) -> Dict:
    """Get the headers and responses from the CSV file"""
    responses = []
    with open(csv_location) as csvfile:
        row = csvfile.readline().split(',')
        headers = {
            "name": row[1],
            "aws": row[2],
            "dev": row[3],
            "ml": row[4]
        }

    with open(csv_location) as csvfile:
        csvfile.readline()
        rows = csv.reader(csvfile)
        for row in rows:
            responses.append([row[1], row[2], row[3], row[4]])

    return headers, responses


def _display_plot(labels, responses, cluster_labels):
    """Plot the responses in 3D"""
    ax = plt.axes(projection='3d')
    plt.gcf().canvas.set_window_title('IW ML immersion day')
    plt.title('Afternoon session groups', color='white')
    plt.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.set_facecolor('#354048')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.tick_params(axis='z', colors='white')

    limits = [0, 10]
    ax.set_xlim(limits)
    ax.set_ylim(limits)
    ax.set_zlim(limits)
    ax.set_xlabel(labels.get("aws"), color='white')
    ax.set_ylabel(labels.get("dev"), color='white')
    ax.set_zlabel(labels.get("ml"), color='white')

    x = [int(row[1]) for row in responses]
    y = [int(row[2]) for row in responses]
    z = [int(row[3]) for row in responses]

    # The prism colour map provides better visual contrast for 2 groups,
    # but due to its cyclical pattern it doesn't work so well for
    # larger numbers of groups. gist_rainbow works better in that case.
    colour_map = "prism" if len(set(cluster_labels)) == 2 else "gist_rainbow"
    ax.scatter3D(x, y, z, c=cluster_labels, cmap=colour_map)
    plt.show()


def _kmeans(responses, num_groups) -> List:
    """Cluster the respondents into two groups"""
    data = [response[1:] for response in responses]
    labels = KMeans(n_clusters=int(num_groups)).fit_predict(data)
    return list(labels)


def _print_group_lists(responses, labels):
    """Print the group members to the console"""
    groups = defaultdict(list)
    for row in zip([i[0] for i in responses], labels):
        groups[row[1]].append(row[0])

    pp = pprint.PrettyPrinter()
    pp.pprint(groups)


def main():
    args = _parse_args()
    csv_location = args.csv
    headers, responses = _load_responses(csv_location)
    cluster_labels = _kmeans(responses, args.groups)
    _print_group_lists(responses, cluster_labels)
    _display_plot(headers, responses, cluster_labels)


if __name__ == '__main__':
    main()
