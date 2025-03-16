import re

from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('page-01.html', 'r', encoding='utf-8') as file:
        html = file.read()
        soup = BeautifulSoup(html, 'lxml')

        # print(soup.prettify())
        result = soup.title.string
        print(result)
        # soup case page01
        result = soup.title.get_text()
        print(result)
        # soup case page01

        result = soup.nav.a.get('href')
        print(result)
        # https://www.baidu.com/

        result = soup.find_all('a', href='#about')
        print(result)
        # [<a href="#about">page01 about</a>]

        result = soup.find_all('a', string=re.compile('page01 nav'))
        print(result)
        # [<a href="https://www.baidu.com/">page01 nav</a>]

        result = soup.select("#special-remind > strong")
        print(result)
        # [<strong>page01 strong</strong>]
