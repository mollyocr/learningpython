### 2018-12-13 mollyocr
#### practicepython.org exercise 17: decode a web page

## Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage:
## http://www.nytimes.com/

#### DONE: Installed requests http://docs.python-requests.org/en/latest/
# Actually, installed pipenv, then installed requests
import requests
url = 'http://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

#### "Requests was developed with some PEP 20 idioms in mind" which I quite like and am capturing here:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Readability counts.

#### DONE: Installed BeautifulSoup https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Actually, upgraded pip - pip3, actually - then installed BeautifulSoup, then installed html5lib
from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, "html5lib")

#### Does this shit work??
# print(soup.prettify()) # Yes!

#### So just to screw my head on, I'm just walking through the BeautifulSoup documentation, and this is a good starting point for what I'm trying to achieve --
# for link in soup.find_all('a'):
#     print(link.get('href'))

#### Ok so now what? Go look at the HTML for NYT page to see how article titles are marked.

headlines = soup.find_all(class_="css-6h3ud0 esl82me2") # I don't actually think I'm grabbing ALL articles titles; there are different ones in use all over -- I'm just going to plow ahead with this because hey it's working and I don't want to spend time not sleeping so I can learn the information architecture of NYT's site, ugh.

# print(headlines) # This works but it's really ugly!

for headline in headlines: # A neater way to spit it out
    print(headline.contents[0]) # And contents just gives the contents!

#### I think I fucking did it?!
