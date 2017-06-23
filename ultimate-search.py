from bs4 import BeautifulSoup
import requests
import sys
import webbrowser
import time

if len(sys.argv)<2:
    print("Usage: python ultimate-search.py <your search>")
    sys.exit(0)
else:
    term = " ".join(sys.argv[1:])
    search_term = "https://www.google.com/search?q="+term
    res = requests.get(search_term)
    print("Googling...")
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html5lib")
    links_to_search = soup.select(".r a")
    numOpen = min(5, len(links_to_search))
    for i in range(numOpen):
        webbrowser.open("http://google.com" + links_to_search[i].get("href"))
        time.sleep(2)