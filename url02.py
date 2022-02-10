from bs4 import BeautifulSoup
import urllib.request as req

url_1 = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109"
result_1 = req.urlopen(url_1)
soup= BeautifulSoup(result_1, 'html.parser')
for location in soup.select("location") :
    #내부의 city, wf, tmn, tmx 태그를 찾아 출력
    print("도시 : ", location.select_one("city").string)
    print("날시 : ", location.select_one("wf").string)
    print("최저기온 : ", location.select_one("tmn").string)
    print("최고기온 : ", location.select_one("tmx").string)
