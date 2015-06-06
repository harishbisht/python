__author__ = 'Harish'
import requests
from bs4 import BeautifulSoup
url = "http://www.imdb.com/movies-in-theaters/"
r = requests.get(url)
soup = BeautifulSoup(r.content)
links = soup.find_all("div", {"class": "list_item"})
for link in links:
    print ("\n\n*************movie****************\n")
    title = link.find("h4", {"itemprop": "name"}, True)
    print "movie name : " + title.text
    mins =link.find("time", {"itemprop": "duration"}, True)
    print "movie time : " + mins.text
    type =link.find("span", {"itemprop": "genre"}, True)
    print "genre : " + type.text
    rating = link.find("div", {"class": "rating_txt"}, True)
    print "rating : " + rating.find("strong").string + "/100"

    stars = link.find_all("div", {"class": "txt-block"}, True)
    #print stars
    print "stars are : "
    for i in stars:
        s = i.find_all("span", {"itemprop": "actors"})
        for i in s:
            print i.text.strip()



