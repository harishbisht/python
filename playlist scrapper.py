__author__ = 'Harish'
import requests
from bs4 import BeautifulSoup
url = 'https://www.youtube.com/playlist?list=PLEsfXFp6DpzR6FatOy4RtoXfu4PeYO_RL'
r = requests.get(url)
soup = BeautifulSoup(r.content)
links = soup.find_all("tr", {"class": "pl-video"})
for link in links:
    print link.get("data-title")
    print "https://www.youtube.com/watch?v=" + link.get("data-video-id")


