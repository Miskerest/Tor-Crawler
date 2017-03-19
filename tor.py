import requests

proxies = {
    'http': 'localhost:8118',
    'https': 'localhost:8118'
}

print "Tor IP: " + requests.get("http://icanhazip.com").text

url = "http://duskgytldkxiuqc6.onion/"


print "test: " + requests.get(url).text


