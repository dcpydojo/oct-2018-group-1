import json
import sys

def translated_phrase(phrase, lang):
    t = hit_the_api(phrase, lang)
    return t

def translate(phrase,
              from='en',
              to_languages=['spanish','chinese','russian']):
    for lang in to_languages:
        phrase = translated_phrase(phrase, lang)
    return phrase

if __name__ == '__main__':
    translation = translate('success')
    print(translation)
