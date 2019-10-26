# Natural Language Processing (NLP) demo
**Dr. Chris Empson, Infinity Works Ltd.**

[chris.empson@infinityworks.com](mailto:chris.empson@infinityworks.com)

LinkedIn: <https://www.linkedin.com/in/chris-empson-45881019/>

## Overview
This demo demonstrates natural language processing by identifying the entities (people, places etc) that feature in a selected Wikipedia page.

The Wikipedia page is downloaded using the Wikipedia API, then the Python Natural Language Toolkit (NLTK) is used to analyse the text.

The text is decomposed into sentences, and the words are annotated with position tags (e.g. noun, proper noun, verb.) NLTK's built-in grammar is then used to identify sequences of words that look like the names of people, places etc.

## Running the demo
This demo requires more dependencies than the other demos. Since there is no GUI it is easiest to run it using Docker.

You will need python3, numpy, scipy, scikit-learn, the Python Natural Language Toolkit and some other dependencies.

Build the demo with:

```docker-compose build```

This can take a little while because some of the dependencies require compilation. 

Once the container build is complete you can run the demo by running the script with the name of a person or thing that has a Wikipedia page, e.g.:

```docker-compose run nlp python3 nlp.py "Carl Sagan"```

