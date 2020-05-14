from bs4 import BeautifulSoup
from requests import get
import urllib.parse

def MegogoFind(name):
    url = f"https://megogo.ru/ru/search-extended?q={urllib.parse.quote(name)}"
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movies = html_soup.find_all('div', class_ = 'card-content video-content', limit=2)
    result = []

    for mv in movies:
        movie_obj = {'name': mv.find('h3', class_='video-title').text.strip(), 'link': "https://megogo.ru" + mv.find('a')['href']}
        mv_html_soup = BeautifulSoup(get(movie_obj['link']).text, 'html.parser')


        price = mv_html_soup.find('div', class_='btn-description')
        if price is None:
            movie_obj['price'] = '-'
        else:
            movie_obj['price'] = price.text
        
        result.append(movie_obj)

    print(result)
    return

MegogoFind("Матрица")


#https://megogo.ru/ru/search-extended?q=%D0%BC%D0%B0%D1%82%D1%80%D0%B8%D1%86%D0%B0

#https://megogo.ru/ru/view/2452941-matrica.html