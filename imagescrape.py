from bs4 import BeautifulSoup
from urllib.request import Request,urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.wallpapermaiden.com/category/3d?page=1"

req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'})

html = urlopen(req, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

print(soup)