import urllib
import urllib.request
from urllib.request import urlopen


class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            print('download return none')
            return None

        response = urllib.request.urlopen(url)
        # print(response)

        if response.getcode() != 200:
            return None

        return response.read()


