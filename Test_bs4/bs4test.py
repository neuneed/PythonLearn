#ecoding uft-8

import re
from bs4 import BeautifulSoup

print('\n\n=================BeautifulSoup 解析 ==================== \n\n')
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

#  获取所有的链接
soup = BeautifulSoup(html_doc,'html.parser')

links = soup.find_all('a')
for link in links:
    # print(link)
    print(link.name,link['href'],link.get_text())


# 获取lacie url的链接
link_node = soup.find('a',href ='http://example.com/lacie')
print(link_node.name, link_node['href'], link_node.get_text())


# 正则匹配  模糊匹配
link_node2= soup.find('a',href = re.compile(r"ill"))
print(link_node2.name, link_node2['href'], link_node2.get_text())


# 获取P 段落文字
link_nodep= soup.find('p',class_='title')
print(link_nodep.name, link_nodep.get_text())






