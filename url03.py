from bs4 import BeautifulSoup
import urllib.request as req
url = "https://news.daum.net/"

result = req.urlopen(url)
soup = BeautifulSoup(result, 'html.parser')

news = soup.select("strong.tit_g")

for list in news :
    a = list.select_one("a")
    print("링크 : " + a.attrs['href'])
    title = a.string
    print("제목 : " + title)