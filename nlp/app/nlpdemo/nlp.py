import collections
import logging
import nltk


class Nlp(object):
    """ Extracts named entities from Wikipedia text. """
    related_entities = list()

    def __init__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s',
            level=logging.INFO)

    def process(self, document):
        """ Tag the words in the document and extract the named entities. """
        related_entities = list()
        for sentence in self.tag_words_in_document(document):
            for p in self.get_person_entities(sentence):
                related_entities.append(p)
            for x in self.get_x_of_y_entities(sentence):
                related_entities.append(x)

        # Save the result in the related_entities class variable.
        self.related_entities = [x for x in related_entities]

    def tag_words_in_document(self, document):
        """
        Take a document, break it into sentences and tag the words.
        """
        sentences = nltk.sent_tokenize(document)
        words = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_document = [nltk.pos_tag(word) for word in words]
        return tagged_document

    def find_entities(self, tagged_document, grammarString):
        """
        Return a list of entities in a tagged text using the
        specified NLTK grammar.
        """
        entities = set()
        grammar = 'NAMEDENTITY: {'+grammarString+'}'
        chunk_parser = nltk.RegexpParser(grammar)
        result = chunk_parser.parse(tagged_document)
        for i in result:
            if (isinstance(i, nltk.tree.Tree)):
                entities.add(' '.join([l[0] for l in i.leaves()]))
        return entities

    def get_person_entities(self, tagged_document):
        """
        Get all of the <Proper noun> <Proper Noun> <optional Proper Noun>
        <optional Proper Noun> entities from a tagged document.
        """
        return self.find_entities(tagged_document, '<NNP><NNP><NNP>?<NNP>?')

    def get_x_of_y_entities(self, tagged_document):
        """
        Get all of the 
        <Proper noun> <Linker> <Proper Noun> <optional Proper Noun>
        entities from a tagged document.
        """
        return self.find_entities(tagged_document, '<NNP><IN><NNP><NNP>?')

    def most_relevant_entities(self, limit):
        """
        Returns a list of the entities that appear most frequently in the
        set of related entities.
        """
        return collections.Counter(self.related_entities).most_common(limit)
