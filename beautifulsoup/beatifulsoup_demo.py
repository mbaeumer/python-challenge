from bs4 import BeautifulSoup
from urllib.request import urlopen



# things to check out:
# parser
# prettify
# get_text
# find
# find_all
# has_attr
# findChildren
if __name__ == '__main__':
    print("Hello")
    soup = BeautifulSoup(urlopen("http://www.kicker.de/premier-league/vereine"))
    tds = soup.find_all("td")
    for td in tds:
        print(td)

    tds_clubs = soup.find_all("td",{"class":"kick__t__a__l kick__table--ranking__teamname kick__table--ranking__index kick__respt-m-w-160"})
    for td in tds_clubs:
        print(td.get_text())
        club_link = td.findChildren("a")[0]
        print(club_link.has_attr('href'))