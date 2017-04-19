#!/usr/bin/env python
from nose.tools import *
from JSTPyGame import Parser


def test_peek():
    # check if with an empty word_list
    assert_equal(Parser.peek(""), None)
    # check with a list of one element
    assert_equal(Parser.peek([('noun', 'garde')]), 'noun')
    # check with a list of several element (normal behavior)
    assert_equal(Parser.peek([('stop', 'le'), ('noun', 'hero')]), 'stop')


def test_match():
    # check with an empty word_list
    assert_equal(Parser.match("", 'verb'), None)
    # check if the first element of word_list not corresponds to the expecting word type
    assert_equal(Parser.match([('stop', 'le')], 'verb'), None)
    # check result with the good expecting word type
    assert_equal(Parser.match([('noun', 'hero'), ('verb', 'frappe')], 'noun'), ('noun', 'hero'))


def test_skip():
    # check if all stop words at the begining have been remove from word_list
    word_list = [('stop', 'le'), ('stop', 'la'), ('noun', 'hero')]
    Parser.skip(word_list, 'stop')
    assert_equal(word_list, [('noun', 'hero')])
    # check if Parser.skip() return nothing
    assert_equal(Parser.skip([('stop', 'le'), ('stop', 'la'), ('noun', 'hero')], 'stop'), None)


def test_parse_verb():
    # check normal behavior
    assert_equal(Parser.parse_verb([('stop', 'le'), ('verb', 'frappe')]), ('verb', 'frappe'))
    # check exception raising
    assert_raises(Parser.ParserError, Parser.parse_verb, [('stop', 'le'), ('noun', 'hero')])


def test_parse_object():
    # check normal behavior with noun
    assert_equal(Parser.parse_object([('stop', 'le'), ('noun', 'hero')]), ('noun', 'hero'))
    # check normal behavior with direction
    assert_equal(Parser.parse_object([('stop', 'le'), ('direction', 'droite')]), ('direction', 'droite'))
    # check exception raising
    assert_raises(Parser.ParserError, Parser.parse_object, [('stop', 'le'), ('verb', 'frapper')])


def test_parse_subject():
    # check normal behavior
    test = Parser.parse_subject([('verb', 'frappe'), ('stop', 'le'), ('noun', 'cheval')], ('noun', 'garde'))
    assert_equal(test.subject, 'garde')
    assert_equal(test.verb, 'frappe')
    assert_equal(test.object, 'cheval')


def test_parse_sentence():
    # check normal behavior
    test = Parser.parse_sentence([('stop', 'le'), ('noun', 'hero'), ('verb', 'attaque'),
                                  ('stop', 'le'), ('noun', 'cheval')])
    assert_equal(test.subject, 'hero')
    assert_equal(test.verb, 'attaque')
    assert_equal(test.object, 'cheval')
    # check behavior without subject
    test = Parser.parse_sentence([('verb', 'attaquer'), ('stop', 'le'), ('noun', 'cheval')])
    assert_equal(test.subject, 'player')
    assert_equal(test.verb, 'attaquer')
    assert_equal(test.object, 'cheval')
    # check exception raising
    assert_raises(Parser.ParserError, Parser.parse_sentence, [('direction', 'nord'), ('stop', 'le'), ('noun', 'cheval')])


