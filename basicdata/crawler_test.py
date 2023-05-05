import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/top250'

movie_list = []

for i in range(0, 100, 25):
    params = {'start': str(i), 'filter': ''}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='item')
    for item in items:
        title = item.find('span', class_='title').text
        rating = item.find('span', class_='rating_num').text
        content = item.find('span', class_='inq').text
        movie_list.append({'title': title, 'rating': rating, 'content': content})

for movie in movie_list:
    print(movie['title'], movie['rating'], movie['content'])
