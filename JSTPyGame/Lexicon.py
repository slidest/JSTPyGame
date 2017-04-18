lexicon = {
            'verbs': [
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
                    'frappes',
                    ],
            'noons': [
                    'cheval',
                    'garde',
                    'gravier',
                    'caillou'
                    ],
            'stops': [
                    'le',
                    'la',
                    'avec',
                    'sur',
                    'du'
                    ]
          }


def convert_number(string):
    try:
        return int(string)
    except ValueError:
        return None


def scan(sentence):
    words = sentence.lower().split()
    analysed_words = []
    for word in words:
        if word in lexicon['verbs']:
            analysed_words.append(('verb', word))
        elif word in lexicon['noons']:
            analysed_words.append(('noon', word))
        elif word in lexicon['stops']:
            analysed_words.append(('stop', word))
        else:
            number = convert_number(word)
            if number is None:
                analysed_words.append(('error', word))
            else:
                analysed_words.append(('number', number))
    return analysed_words
