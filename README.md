# Tor-Crawler
Basic setup to install a web crawler for the Tor network


# Requirements

* Tor
* Polipo
* Python + Pip

# Setup 

Download Tor & Polipo HTTP proxy

`sudo apt install tor polipo`

Start both of them in daemon mode

`tor &`

`polipo &`

Change the configuration of `/etc/polipo/config` to that of `polipo.conf` (included)

Polipo will run on port 8118, Tor on the default port of 9050.

Test a request

`curl --proxy localhost:8118 http://duskgytldkxiuqc6.onion/`

If configured correctly, cURL will return an HTML document. Note that the tested .onion address must be operational.
