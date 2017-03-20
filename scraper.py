### NOTE: WORK IN PROGRESS - NOT CURRENTLY FUNCTIONAL ###


import requests
import scrapy
import re
from BeautifulSoup import BeautifulSoup
import shutil

proxies = { 
     'http': 'localhost:8118',
     'https': 'localhost:8118'
}


def download(url):
	print "Trying download of address: " + url
	file = requests.get(url, proxies=proxies, stream=True)
	with open(url[-10:], 'wb') as f:
	        for chunk in file.iter_content(chunk_size=1024): 
        	    if chunk: # filter out keep-alive new chunks
                	f.write(chunk)

def getTags(response):
	soup = BeautifulSoup(response)
	for tag in soup.findAll('a', href=True):
		ext = re.findall('"([^"]*)"', str(tag))
	return ext

print "Tor IP: " + requests.get("http://icanhazip.com").text

url = "http://zqktlwi4fecvo6ri.onion/wiki/index.php/Main_Page"

# url of sample warez: http://cerberussssc7cat.onion/

url = raw_input("Enter URL to scrape: ")

response = requests.get(url+'index.php?path=Crypters', proxies=proxies).text

links = getTags(response)
for link in links:
	links += re.findall('"([^"]*)"', link)

for link in links:
	if "download.php" in link:
		download(url + link)
