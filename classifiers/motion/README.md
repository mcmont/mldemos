# Motion classification demo
**Dr. Chris Empson, Infinity Works Ltd.**

chris.empson@infinityworks.com

Twitter: [@monty_mcmont](https://twitter.com/monty_mcmont)

## Overview
This demo demonstrates how to collect data and classify it in real time. 

The demo starts an HTTP server which serves an HTML file. The user connects to the server via a mobile device that contains accelerometers. The embedded Javascript code reads the device's accelerometers and read the magnitude of the motion in the x, y and z axes. Data is held in an array until it contains 25 data samples for each axis. The device then calculates the mean and standard deviation of the data, and sends it to the server via an HTTP POST request.

The included training data "teaches" the classifier using example data that is received during various activities; sitting, standing, holding the device in the hand, jogging on the spot and shaking the device. Please note that this data may have different characteristics for different people. For example I tend to keep my phone in my right trouser pocket, so my phone tends to be in a certain orientation when I sit down. If you keep yours in your left pocket the orientation may differ, and you may see wrong results. (This is only a demo, deal with it... or fork the code and improve it!)

The model uses a *k*-nearest neighbours search to find the closest data points from the training set. The value of *k* is set to 5 by default. The majority classification of the 5 closest training data points is reported as the type of motion detected.

*k*-nearest neighbours is somewhat unusual in machine learning because *all* of the training data is used in the model; splitting the data into training and validation sets only reduces the accuracy of the model.

## Running the demo
You will need python3 and scikit-learn to run this demo. You will also need a mobile device. This demo was tested using an iPhone 6S which reports new accelerometer readings every 16.7ms.

Run the HTTP server:
```python3 server.py OPTIONAL_PORT_NUMBER```

Then connect to the server at the specified port number using your mobile device. If no port number is specified the server will use port 8000.

## References

[Activity Recognition with Smartphone Sensors](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6838194)

[Activity Recognition using Cell Phone Accelerometers](http://www.cis.fordham.edu/wisdm/public_files/sensorKDD-2010.pdf)

[Sensing Meets Mobile Social Networks: The Design,
Implementation and Evaluation of the CenceMe
Application](http://sensorlab.cs.dartmouth.edu/pubs/cenceme_sensys08.pdf)

