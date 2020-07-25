import requests
from bs4 import BeautifulSoup

#python코드가 아니라 사람이넉하려고 넣는 경우가 많다
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36' }
#ajax를 한것같이 데이터를 불러오는 부분
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)
#data.text html파일 전체의 내용이 다 들어가 있어요.
#'htmle.parser'는 파싱작업을 우리 대신 해준다
#파싱이란 텍스트 파일을 프로그래밍 언어에 있는 구조(ex dictionary,list)에 넣어주는 것이다.
soup=BeautifulSoup(data.text,'html.parser')
#soup에는 html이 들어간다

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a_tag = movie.select_one('td.title>div>a')
    point = movie.select_one('td.point')


    if a_tag is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        print(rank,a_tag.text,point.text)
