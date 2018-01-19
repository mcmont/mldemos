# Machine Learning Demos
**Dr. Chris Empson, Infinity Works Ltd.**

chris.empson@infinityworks.com

Twitter: @monty_mcmont

## Introduction
These demos will feature in an upcoming beginner-level talk about Artificial Intelligence and Machine Learning.

## Installation
You will need python3, scikit-learn and pyplot to run these demos.

To style the plots in the intended manner copy matplotlib-stylelib/iw.mplstyle to your matplotlib style library, e.g.:

```mkdir -p ~/.matplotlib-conf/stylelib/ && cp matplotlib-stylelib/iw.mplstyle ~/.matplotlib/stylelib/```

Unfortunately it is tricky to Dockerise these demos (believe me, I tried...) because they rely on access to the host device's X11 display. This is actually relatively strighforward on Linux host systems, but it is problematic on OS X and relies on a specific version of Xquartz being installed. To avoid user frustration I decided not to add a Dockerfile. Sorry.

## Running the demos
If you have python3, scikit-learn and matplotlib already installed you can simply run the demos directly, e.g.:
```python3 svm_linear.py```

## TODO
* Add neural network demos
* Add natural language processing demos

## References and useful links

http://scikit-learn.org/stable/modules/svm.html

https://mubaris.com/2017/10/14/svm-python/

https://stackoverflow.com/questions/23794277/extract-decision-boundary-with-scikit-learn-linear-svm
