import requests
import re

api_key = "bfb84a4870188408329911df322f4f6f7ad3dcac830b9e8531912c909d410dc4"

def download_sample(sha1):
    r = requests.post('http://malshare.com/pull.php',data={'api_key':api_key,'hash':sha1})
    data = r.content
    r.close()
    f = open(sha1,'w')
    f.write(data)
    f.close()
    print "[+] Downloaded: " + sha1

def grab_hashes():
    sha1_hashes = []
    r = requests.get('http://malshare.com/daily/malshare.current.sha1.txt')
    li = r.content
    r.close()
    li = li.split('\n')
    for h in li:
        if h != "":
            sha1_hashes.append(h)

    if len(sha1_hashes) == 0:
        url = raw_input("Enter URL for list of hashes: ")
        r = requests.get(url)
        li = r.content
        r.close()
        li = li.split('\n')
        for h in li:
            if h != "":
                sha1_hashes.append(h)
    
    return sha1_hashes

def main():
    print "[+] Initiating download..."
    print "[+] Grabbing today's sample hash list..."
    hashes = grab_hashes()
    for h in hashes:
        download_sample(h)

def extract_emails(hash):
    print "[+] Searching for emails..."
    f = open(hash, 'r')
    match = re.findall(r'[\w\.-]+@[\w\.-]+', f.read())
    print match


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print "\n\n[+] Goodbye"
