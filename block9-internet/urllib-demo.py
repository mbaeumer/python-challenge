import urllib.request
import sys

def get_website():
    try:
        url = "http://www.kicker.de"
        with urllib.request.urlopen(url) as doc:
            html = doc.read()
            print(html)
    except:
        print("Error", file=sys.err)

if __name__ == '__main__':
    get_website()