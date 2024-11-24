import json
import os

from get_project_root import root_path



class Translate:
    availlables: list = ['en', 'fr']

    @classmethod
    def use(cls, session, lang: str) -> None:
        session.setdefault('lang', 'en')
        session['lang'] = 'en'

        if lang in cls.availlables and lang != 'en':
            session['lang'] = lang

        return None



    @classmethod
    def do(cls, key: str, lang: str, number: int = 1, value: str = None) -> str:
        #arguments
        if lang is None:
            lang = 'en'

        if lang not in cls.availlables:
            print('Warning: lang "' + lang + '" is not available, set it to "en"')
            lang = 'en'

        if key is None:
            print('Error: key is None')
            return '-'

        if number > 1 and key[-1] != 's':
            print('Info: number is greater than 1, set key to pluriel')
            key = key + 's'

        #get translations by lang
        translations: dict = cls.load_file(lang)

        #valid translation found
        if key in translations:
            return cls.replace_value(translations[key], value)

        #find by singular key
        if key[-1] == 's':
            print('Warning: key not found in translation, test it in singular')
            key = key[:-1]

            if key in translations:
                return cls.replace_value(translations[key], value)

        #find by default translations
        if lang != 'en':
            print('Warning: key not found in translation, test it in "en"')
            translations = cls.load_file('en')

            if key in translations:
                return cls.replace_value(translations[key], value)

            #find by plurial key in default translations
            print('Warning: key not found in default translation, test it in pluriel')
            key = key + 's'

            if key in translations:
                return cls.replace_value(translations[key], value)

        print('Error: key not found in all translations')

        return '-'



    @staticmethod
    def load_file(lang: str) -> dict:
        root: str       = root_path()
        file_path: str  = root + '/translation/' + lang + '.json'

        if not os.path.exists(file_path):
            print('Error: file not exist (check your path)')
            return {}

        with open(file_path, 'r') as file:
            translations: dict = json.load(file)

        return translations



    @staticmethod
    def replace_value(string: str, value: str) -> str:
        if '{value}' in string:
            string = string.replace('{value}', value)

        return string
