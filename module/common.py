import os
import requests

from bs4                import BeautifulSoup

from module.translate   import Translate



class Common:
    @staticmethod
    def git_url() -> str:
        return os.getenv('GIT')



    @staticmethod
    def count_commit() -> str:
        url = os.getenv('GIT')

        #parse url for get text with number of commit
        response    = requests.get(url)
        soup        = BeautifulSoup(response.text, 'html.parser')
        span        = soup.find('span', {'class' : 'fgColor-default'}).text

        if span is None or 'Commits' not in span:
            return '666'

        #return only commit value
        results = span.split(' ')

        return str(results[0])



    @staticmethod
    def version(lang: str = 'en') -> str:
        commit = Common.count_commit()

        #format commit
        major = Translate.do(lang = lang, key = 'version') + ' ' + str(os.getenv('VERSION_MAJOR')) + '.'

        if len(commit) > 2:
            return major + commit[:-2] + '.' + commit[-2:]

        elif len(commit) <= 2:
            return major + '0.' + commit

        return major + commit.zfill(2)
