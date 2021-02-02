import os
import sys
import requests
file1 = open(sys.argv[1], 'r')
Lines = file1.readlines()

def url_ok(url):
    try:
        r = requests.get(url,timeout=5)
        if r:
            return True
        return False
    except Exception as e:
        return False


path = "auto-secret-finder"
try:
    os.mkdir(path)
except OSError:
    print ("Creation of the directory %s failed" % path)

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("[ * ] Scanning {}...".format(count))
    if line[:7] == "http://" or line[:8] == "https://":
    	protocol = ""
    else:
    	protocol = "http://"
    if url_ok(protocol + line.strip()):
        os.system("python3 SecretFinder.py -i " + protocol + "{} -o auto-secret-finder/{}.html".format(line.strip(), line.strip()))

# EDIT THIS LAST LINE AS YOU WANT TO FIT YOUR GOALS!
