# Human Pie Divider
**Dr. Chris Empson, Infinity Works Ltd.**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

LinkedIn: <https://www.linkedin.com/in/chris-empson-45881019/>

## Overview

I wanted to divide a group of people into groups with similar levels of expertise.

I asked each person to complete a Google Form in which they rated their knowledge of AWS & machine learning, and whether they identify as more of a data scientist or a developer. On the data scientist / developer axis 0 represents 'data scientist' and 10 represents 'developer'. 

I then exported the responses as a CSV file. Some sample data is included in this repo.

The Python script loads the data from the CSV file, runs a _k_-means clustering algorithm to generate the groups, then visualises the results in 3D.

## Prerequisites
You'll need Python 3 and the `matplotlib` and `scikit-learn` libraries.

```bash
pip install matplotlib scikit-learn
```

## Running the demo

Specify the path of the CSV file and the number of groups on the command line:
```bash
python plot.py --csv path/to/responses.csv --groups 2
```

The group members are printed to the terminal, and a 3D visualisation of the groups is displayed.
