# -*- coding: utf-8 -*-
class French(object):
        verbs = [
                'jeter',
                'lancer',
                'attaquer',
                'frapper',
                'jete',
                'lance',
                'attaque',
                'frappe',
                'jetes',
                'lances',
                'attaques',
                'frappes']

        nouns = [
                'cheval',
                'garde',
                'gravier',
                'caillou',
                'hero']

        stops = [
                'le',
                'la',
                'avec',
                'sur',
                'du',
                'à',
                'en']

        directions = [
                    'gauche',
                    'droite',
                    'haut',
                    'bas',
                    'nord',
                    'sud',
                    'est',
                    'ouest']


def convert_number(string):
    try:
        return int(string)
    except ValueError:
        return None


def scan(player_input):
    words = player_input.lower().split()
    analysed_words = []
    for word in words:
        if word in French.verbs:
            analysed_words.append(('verb', word))
        elif word in French.nouns:
            analysed_words.append(('noun', word))
        elif word in French.stops:
            analysed_words.append(('stop', word))
        elif word in French.directions:
            analysed_words.append(('direction', word))
        else:
            number = convert_number(word)
            if number is None:
                analysed_words.append(('error', word))
            else:
                analysed_words.append(('number', number))
    return analysed_words
