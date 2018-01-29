import certifi
import unwiki
import re
import logging
import wikipedia


class WikipediaDownloader(object):
    """ Download a page from Wikipedia. """

    def __init__(self):
        logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)
        wikipedia.set_lang('en')

    def download_page(self, searchTerm):
        self.page = wikipedia.page(searchTerm)
        document = self.page.content
        logging.info('Downloading Wikipedia page for '+searchTerm)
        return self.unWikifyString(self.stripTags(document))

    def unWikifyString(self, s):
        """ Removes Wiki formatting from a string. """
        unWikifiedString = unwiki.loads(s)
        wordList = unWikifiedString.split()
        i = 0
        while i < len(wordList):
            # Remove words containing a pipe character
            if wordList[i].find('|') > -1:
                del wordList[i]
            else:
                i += 1
        return ' '.join(wordList)

    def stripTags(self, value):
        """ Returns the given HTML with all tags removed. """
        return self.stripCurlyBraceTags((self.stripHtmlTags(value)))

    def stripHtmlTags(self, value):
        """ Returns the given string with all HTML tags removed. """
        return re.sub(r'<[^>]*?>', ' ', value)

    def stripCurlyBraceTags(self, value):
        """ Returns the given string with all curly brace tags removed. """
        return re.sub(r'{{[^}]*?}}', ' ', value)