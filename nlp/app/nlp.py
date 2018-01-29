"""
Natural Language Processing demo.

The argument to this script will be sent to the Wikipedia API.
Assuming that a matching page is found it will be downloaded,
parsed and the named entities extracted.
"""
import argparse
from nlpdemo import wiki, nlp


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    args = parser.parse_args()

    document = wiki.WikipediaDownloader().download_page(args.name)

    nlp = nlp.Nlp()
    nlp.process(document)
    print(nlp.most_relevant_entities(limit=30))
