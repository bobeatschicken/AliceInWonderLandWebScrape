from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

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

soup = BeautifulSoup(html_doc, "html.parser")
sisters = {}
links_list = []
classes_list = []
links_dict = {}
classes_dict = {}

for sister in soup.find_all('a'):
    links_list.append(sister.get('href'))
    classes_list.append(sister.get('class')[0])
    sisters[sister.string] = ''
for key in sisters.keys():
    sisters[key] = {'class' : '', 'link' : ''}
links_list_iter = iter(links_list)
classes_list_iter = iter(classes_list)
for key in sisters.keys():
    sisters[key]['class'] = next(classes_list_iter)
for key in sisters.keys():
    sisters[key]['link'] = next(links_list_iter)
sisters_df = pd.DataFrame(sisters)

print(sisters_df)
