from bs4 import BeautifulSoup
from requests import get
import urllib.parse


def IviFind(name):
    url = f"https://www.ivi.ru/search/?q={urllib.parse.quote(name)}"
    print(url)
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movies = html_soup.find_all('a', class_= 'nbl-slimPosterBlock', limit=2)

    result=[]
    for mv in movies:
        movie_obj = {'name': mv.find('div', class_='nbl-slimPosterBlock__title').text, 'link': "https://www.ivi.ru" + mv['href']}
        mv_html_soup = BeautifulSoup(get(movie_obj['link']).text, 'html.parser')

        rating = mv_html_soup.find('div', class_='ratingBlock__value')
        if rating is None:
            movie_obj['rating']='-'
        else:
            movie_obj['rating']=rating.text

        # Todo: Help parse src from <img> poster
        image = mv_html_soup.find('div', class_='nbl-poster__image')
        if image is None:
            movie_obj['image_url']='-'
        else:
            movie_obj['image_url']=image.src

        price = mv_html_soup.find('del', class_='nbl-button__strikedText')
        if price is None:
            movie_obj['price'] = '-'
        else:
            movie_obj['price'] = f"От {price.text} ₽"

        movie_obj['platform'] = 'Ivi'
        
        result.append(movie_obj)

    return result
    '''for a in movies:
        movie_name = html_soup.find_all('div', class_='nbl-slimPosterBlock__title')

        movie_url = 'https://www.ivi.ru' + a['href']
        movie_response = get(movie_url)
        movie_html_soup = BeautifulSoup(movie_response.text, 'html.parser')
        #movie_name= html_soup.find('video-info')['data-title']
        print(movie_name)
    return '''
