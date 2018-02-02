# Machine Learning Demos
**Dr. Chris Empson, Infinity Works Ltd.**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

Twitter: [@monty_mcmont](https://twitter.com/monty_mcmont)

## Introduction
These demos will feature in an upcoming beginner-level talk about Artificial Intelligence and Machine Learning.

The demos are divided into classifiers (binary, motion detection via *k*-nearest neighbours, radial basis function) and natural language processing (NLP).

## Installation
You will need python3, scikit-learn and pyplot to run these demos.

The NLP demo doesn't require a GUI and has a number of additional dependencies so it may be more convenient to build and run this via the supplied docker-compose file. You will need a recent version of Docker to do this. 

The Support Vector Machine classifier and motion detection demos require a GUI. Unfortunately it is tricky to Dockerise these demos (believe me, I tried...) because they rely on access to the host device's X11 display. This is actually relatively strighforward on Linux host systems, but it is problematic on OS X and relies on a specific version of Xquartz being installed. To avoid user frustration I decided not to add a Dockerfile.

To style the plots in the intended manner copy matplotlib-stylelib/iw.mplstyle to your matplotlib style library, e.g.:

```mkdir -p ~/.matplotlib-conf/stylelib/ && cp matplotlib-stylelib/iw.mplstyle ~/.matplotlib/stylelib/```

## Running the demos
### 
If you have python3, scikit-learn and matplotlib already installed you can simply run the demos directly, e.g.:
```python3 classifiers/support-vector-machine/svm_lemon_or_banana.py```


## References, useful links and whatnot

### Support Vector Machines
http://scikit-learn.org/stable/modules/svm.html

https://mubaris.com/2017/10/14/svm-python/

https://stackoverflow.com/questions/23794277/extract-decision-boundary-with-scikit-learn-linear-svm

### Motion recognition
[Activity Recognition with Smartphone Sensors](http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=6838194)

[Activity Recognition using Cell Phone Accelerometers](http://www.cis.fordham.edu/wisdm/public_files/sensorKDD-2010.pdf)

[Sensing Meets Mobile Social Networks: The Design,
Implementation and Evaluation of the CenceMe
Application](http://sensorlab.cs.dartmouth.edu/pubs/cenceme_sensys08.pdf)

### Neural Networks
[Layers in TensorFlow](https://katacoda.com/basiafusinska/scenarios/tensorflow-layers) - Sample code to build a convolutional neural network to solve the NMIST classification problem in TensorFlow, by Barbara Fukinska.
