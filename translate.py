import json
import sys


def translated_phrase(phrase, lang):
    t = hit_the_api(phrase, lang)
    return t


def translate(phrase, origin_lang='en',
              to_languages=['spanish', 'chinese', 'russian']):
    for lang in to_languages:
        phrase = translated_phrase(phrase, lang)
    return phrase


if __name__ == '__main__':
    phrase = sys.argv[1]
    language = sys.argv[2]
    # translation = translate('success')
    print(sys.argv[0])
    print(f"{phrase} --{language}")
