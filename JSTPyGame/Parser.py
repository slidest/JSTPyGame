# -*- coding: utf-8 -*-


class ParserError(Exception):
    pass


class Sentence(object):

    def __init__(self, subject, verb, obj):
        # remember we take ('noun', 'hero') tuples and convert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]


def peek(word_list):
    """ Return the word type of the first tuple in word_list else return None"""

    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None


def match(word_list, expecting):
    """Return the first tuple in word_list if the word type corresponds to expecting else return None"""

    if word_list:
        word = word_list.pop(0)
        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None


def skip(word_list, word_type):
    """Remove the first element of word_list if it's match the word type give as argument"""
    while peek(word_list) == word_type:
        match(word_list, word_type)


class Parser(object):
    """Class with all methods to parse player inputs after the first analysis by the lexicon module"""

    @staticmethod
    def parse_verb(word_list):
        skip(word_list, 'stop')

        if peek(word_list) == 'verb':
            return match(word_list, 'verb')
        else:
            raise ParserError("Expected a verb next")

    @staticmethod
    def parse_object(word_list):
        skip(word_list, 'stop')
        next = peek(word_list)

        if next == 'noun':
                return match(word_list, 'noun')
        if next == 'direction':
            return match(word_list, 'direction')
        else:
            raise ParserError("Expected a noun next.")

    @staticmethod
    def parse_subject(word_list, subj):
        verb = Parser.parse_verb(word_list)
        obj = Parser.parse_object(word_list)

        return Sentence(subj, verb, obj)

    @staticmethod
    def parse_sentence(word_list):
        skip(word_list, 'stop')

        start = peek(word_list)

        if start == 'noun':
            subj = match(word_list, 'noun')
            return Parser.parse_subject(word_list, subj)
        elif start == 'verb':
            # assume the subject is the player then
            return Parser.parse_subject(word_list, ('noun', 'player'))
        elif start == 'error':
            return Warning("Désolé je ne connait pas ce mot: {}".format(match(word_list, 'error')[1]))
        else:
            raise ParserError("Must start with subject, object, or verb not:{}".format(start))



