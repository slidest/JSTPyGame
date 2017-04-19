#!/usr/bin/env python
from nose.tools import *
from JSTPyGame import Lexicon


def test_nouns():
    assert_equal(Lexicon.scan("cheval"), [('noun', 'cheval')])
    result = Lexicon.scan("garde gravier caillou")
    assert_equal(result, [('noun', 'garde'),
                          ('noun', 'gravier'),
                          ('noun', 'caillou')])


def test_directions():
    assert_equal(Lexicon.scan("nord"), [('direction', 'nord')])
    result = Lexicon.scan("nord sud est")
    assert_equal(result, [('direction', 'nord'),
                          ('direction', 'sud'),
                          ('direction', 'est')])


def test_verbs():
    assert_equal(Lexicon.scan("jeter"), [('verb', 'jeter')])
    result = Lexicon.scan("lancer attaquer frapper lance lances attaque attaques frappe frappes jete jetes")
    assert_equal(result, [('verb', 'lancer'),
                          ('verb', 'attaquer'),
                          ('verb', 'frapper'),
                          ('verb', 'lance'),
                          ('verb', 'lances'),
                          ('verb', 'attaque'),
                          ('verb', 'attaques'),
                          ('verb', 'frappe'),
                          ('verb', 'frappes'),
                          ('verb', 'jete'),
                          ('verb', 'jetes')
                          ])


def test_stops():
    assert_equal(Lexicon.scan("le"), [('stop', 'le')])
    result = Lexicon.scan("la avec sur du")
    assert_equal(result, [('stop', 'la'),
                          ('stop', 'avec'),
                          ('stop', 'sur'),
                          ('stop', 'du')])


def test_numbers():
    assert_equal(Lexicon.scan("1"), [('number', 1)])
    result = Lexicon.scan("123 987 456")
    assert_equal(result, [('number', 123),
                          ('number', 987),
                          ('number', 456)])


def test_errors():
    assert_equal(Lexicon.scan("@"), [('error', '@')])
    result = Lexicon.scan("choucroute gdterel prout")
    assert_equal(result, [('error', 'choucroute'),
                          ('error', 'gdterel'),
                          ('error', 'prout')])
