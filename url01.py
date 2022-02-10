import urllib.request

url="https://www.google.co.kr/images/branding/googlelogo/2x/googlelogo_light_color_272x92dp.png"

imgName = "c://Users/lg/google.png"

urllib.request.urlretrieve(url, imgName)

print("저장 완료")
from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1 id="title">안녕하세요</h1>
        <p id="name">장성원입니다</p>
    </body>
    </html>
"""
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h1')
name = soup.find('p')
print("title : " + title.string)
print("name : " + name.string)
# h1 = soup.html.body.h1
# p = soup.html.body.p
# print("h1 : " + h1.string)
# print("p : " + p.string)