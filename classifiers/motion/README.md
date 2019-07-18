# Motion classification demo
**Dr. Chris Empson, [Infinity Works](https://www.infinityworks.com/)**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

Twitter: [@monty_mcmont](https://twitter.com/monty_mcmont)

LinkedIn: [Chris Empson](https://www.linkedin.com/in/chris-empson-45881019/)

## Overview
This demo demonstrates how to collect accelerometer data from a mobile device and use it to classify what the user is doing, in real time. 

The device does some edge processing on the data to reduce the number of readings that need to be transmitted to a desktop computer for classification.

The device takes 25 readings from the accelerometer sensors, then calculates the mean and standard deviation. The iPhones that this demo was tested with take accelerometer readings every 16.7ms, so 25 readings = 417.5ms of data. 

Training data is included for sitting, standing, waving, walking, jogging on the spot, vigorous shaking, and holding the device in the hand.

## How it works

The demo starts an HTTP server which serves an HTML file. The user connects to the server via a mobile device with accelerometers. The embedded Javascript code acquires data from the device's accelerometers to find the magnitude of the motion in the x, y and z axes. Data is accumulated in an array until it contains 25 data samples for each axis. The device then calculates the mean and standard deviation of the data, and sends it to the server via an HTTP POST request.

The included training data "teaches" the classifier what the accelerometer data looks like during various activities; sitting, standing, holding the device in the hand, jogging on the spot and shaking the device. Please note that this data may have different characteristics for different people. For example I tend to keep my phone in my right trouser pocket, so my phone tends to be in a certain orientation when I sit down. If you keep yours in your left pocket the orientation may differ, and you may see wrong results. (This is only a demo, deal with it... or [fork the code](https://github.com/mcmont/mldemos/tree/master/classifiers#fork-destination-box) and improve it!)

The model uses a _k_-nearest neighbours search to find the closest data points from the training set. The value of *k* is set to 5 by default. The majority classification of the 5 closest training data points is displayed in a window.

_k_-nearest neighbours is somewhat unusual in machine learning because *all* of the training data is used in the model; splitting the data into training and validation sets only reduces the accuracy of the model.

## Running the demo
This demo is written in Python 3. Assuming this is already installed you will need to install scikit-learn and its dependencies. 

```pip3 install numpy && pip3 install scipy && pip3 install scikit-learn```

You will also need a mobile device. This demo was tested using an iPhone 6S and an iPhone 8 Plus which produce new accelerometer readings every 16.7ms.

Since iOS 12.3 Apple has started to prevent insecure websites from using accelerometer data from a device. HTTPS connections are able to access the data, however this no longer appears to work in Safari, even with the "Motion and Orientation Access" option enabled in the Safari settings. Google Chrome works as of iOS 12.3.1.  

To create a TLS certificate for the server, run:
```make certs```

To run the demo:
```make run-iphone```

Then, using your mobile device, connect to the server over `https://` using the displayed port number.

## Generating new training data
If you want to teach the classifier a new class, or if you want to generate training data for a non-iPhone device, you can run the program in training mode by running:

```make train```

The program will print data to the console that can be copied & pasted into a csv file of training data. You'll just need to add a class to the end of each line.

Ensure that there are no empty lines at the end of the file, or numpy will raise ValueError exceptions like:

`ValueError: all the input array dimensions except for the concatenation axis must match exactly`
 

## Related reading & examples

[Activity Recognition with Smartphone Sensors](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6838194)

[Activity Recognition using Cell Phone Accelerometers](http://www.cis.fordham.edu/wisdm/public_files/sensorKDD-2010.pdf)

[Sensing Meets Mobile Social Networks: The Design,
Implementation and Evaluation of the CenceMe
Application](http://sensorlab.cs.dartmouth.edu/pubs/cenceme_sensys08.pdf)

[Simple Python HTTP(S) Server With GET/POST Examples](https://blog.anvileight.com/posts/simple-python-http-server/)

[Alberto Sarullo's Accelerometer Javascript Test](http://www.albertosarullo.com/demos/accelerometer/)
