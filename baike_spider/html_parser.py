import re
import urllib
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):

        new_urls = set()

        # /view/123.htm 此处去拼接
        links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))

        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):

        res_data = {}

        # url
        res_data['url'] = page_url

        #   <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find("dd", attrs={"class": "lemmaWgt-lemmaTitle-title"}).find("h1")
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', attrs={"class": "lemma-summary"})
        res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_count):
        # print('parse123')
        if page_url is None or html_count is None:
            return
        
        soup = BeautifulSoup(html_count , 'html.parser')
        new_urls = self._get_new_urls(page_url ,soup)
        new_data = self._get_new_data(page_url ,soup)
        return new_urls ,new_data

