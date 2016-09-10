#This example is different from book, because my environment is python2
import urllib
import urllib2
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(),"html.parser") #if not have "html parser, warning
print bsObj.h1
