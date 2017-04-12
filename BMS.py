import sys
import requests
from bs4 import BeautifulSoup
def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)
print("This script searches movies around the given location and language.")
base_url = "https://in.bookmyshow.com/"
city = input("Enter city: ")
language = input("Enter language: ")
url = base_url + city +"/movies/" + language
BMS_r = requests.get(url)
print(BMS_r.status_code)
BMS_soup = BeautifulSoup(BMS_r.text, 'html.parser')
uprint(BMS_soup.findAll('a'))
for name in BMS_soup.findAll('div',{'class':'__name overflowEllipses'}):
	uprint(name.text)
