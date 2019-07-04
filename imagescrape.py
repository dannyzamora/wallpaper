from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import Request,urlopen
from urllib.parse import urlparse
import ssl
import random
import re
import os

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def Scape():
    url = lookforimage()
    path = saveImg(url)
    return path

def lookforimage():
    num = random.randint(1,54)
    url = "https://www.wallpapermaiden.com/category/city?page="+str(num)
    print("Starting URL:",url)

    req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req, context=ctx).read()
    print("Home Start....")
    product = SoupStrainer('div',{"class":"wallpaperList"})
    soup = BeautifulSoup(html,'html.parser',parse_only=product)
    links = soup.find_all('a',href=True)
    r = random.choice(links) 
    url = r['href']
    print("Home FIN....")


    for i in range(2):
        print("Stating",i)
        req = Request( url,  headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req, context=ctx).read()
        product = SoupStrainer('div',{"class": re.compile('wpBig *')})
        soup = BeautifulSoup(html, "html.parser",parse_only=product)
        imgs = soup.find('div',{"class": re.compile('wpBig *')})
        links = imgs.find('a',href=True)
        url = links['href']
        print("Ending",i)

    print(url)
    return(url)

def createFolder():
    if not os.path.exists("backgrounds"):
        os.makedirs("backgrounds")

def saveImg(imgurl):
    createFolder()
    print(imgurl)
    print(urlparse(imgurl).path)
    path = urlparse(imgurl).path
    path=os.path.split(path)
    path = "backgrounds/"+path[1]
    req = Request(imgurl,  headers={'User-Agent': 'Mozilla/5.0'})
    open(path, "wb").write(urlopen(req).read())
    return path


