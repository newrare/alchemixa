import os
import requests

from bs4 import BeautifulSoup



class Common:
    @staticmethod
    def get_git_url():
        return os.getenv('GIT')



    @staticmethod
    def count_commit():
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
    def get_version():
        commit = Common.count_commit()

        #format commit
        major = 'Version ' + str(os.getenv('VERSION_MAJOR')) + '.'

        if len(commit) > 2:
            return major + commit[:-2] + '.' + commit[-2:]

        elif len(commit) <= 2:
            return major + '0.' + commit

        return major + commit.zfill(2)



    @staticmethod
    def get_image_url(image):
        #if url end with /, remove it
        url = os.getenv('URL')

        if url[-1] == '/':
            url = url[:-1]

        return url + '/public/image/' + image
