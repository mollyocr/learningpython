### 2019-01-03 mollyocr
#### practicepython.org exercise 19: decode a web page two

## Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

## The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

## This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.

import requests
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, "html5lib")

#### Does this shit work??
print(soup.prettify()) # Yes!

#### Class info for ref
# class="article-main col-md-8 col-xl-9 col-auto article-content-body"

#### So this sort of almost works
# article_all = soup.find_all(class_="content paywall drop-cap")
# for paragraph in article_all:
#     print(paragraph.contents)

#### This doesn't do what I want it to
# article_all = soup.has_attr(data-reactid)
# for paragraph in article_all:
#     print(paragraph.contents)

#### Nope, doesn't do what you want it to
# article_all = soup.find_all("p", string="data-reactid")

#### Ok simplify
article_all = soup.find_all("p")

for paragraph in article_all:
    print(paragraph.contents[0])

#### The end of the output looks good -- just the content of the <p> tags but there's a whole bunch of shit at the front that needs to be cut out and there's some footer to chop off. Need to filter through a class but unghhhh
