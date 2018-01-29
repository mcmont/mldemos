# Machine Learning Demos
**Dr. Chris Empson, Infinity Works Ltd.**

chris.empson@infinityworks.com

Twitter: @monty_mcmont

## Introduction
These demos will feature in an upcoming beginner-level talk about Artificial Intelligence and Machine Learning.

The demos are divided into classifiers, natural language processing (NLP), and anomaly detection.

## Installation
You will need python3, scikit-learn and pyplot to run these demos.

Demos that don't require a GUI (NLP) can be built using docker-compose and run from within the Docker container. Th

The Support Vector Machine classifier demos and the anomaly detection demos require a GUI. Unfortunately it is tricky to Dockerise these demos (believe me, I tried...) because they rely on access to the host device's X11 display. This is actually relatively strighforward on Linux host systems, but it is problematic on OS X and relies on a specific version of Xquartz being installed. To avoid user frustration I decided not to add a Dockerfile.

To style the plots in the intended manner copy matplotlib-stylelib/iw.mplstyle to your matplotlib style library, e.g.:

```mkdir -p ~/.matplotlib-conf/stylelib/ && cp matplotlib-stylelib/iw.mplstyle ~/.matplotlib/stylelib/```

## Running the demos
### 
If you have python3, scikit-learn and matplotlib already installed you can simply run the demos directly, e.g.:
```python3 svm_linear.py```

## TODO
* Add neural network demo
* Add anomaly detection demo

## References and useful links

http://scikit-learn.org/stable/modules/svm.html

https://mubaris.com/2017/10/14/svm-python/

https://stackoverflow.com/questions/23794277/extract-decision-boundary-with-scikit-learn-linear-svm

