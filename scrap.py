import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/list/ls055592025/')
page_contents = r.text
doc = BeautifulSoup(page_contents, 'html.parser')
"MOVIE NAMES "
# movie_names = doc.find_all('h3', class_='lister-item-header')
# for ele in movie_names:
    # Find the 'a' tag within the 'h3' tag and then access its text
#  print(ele.find('a').text)


"YEAR "
# movies_year = doc.find_all('span', class_='lister-item-year text-muted unbold')
# for year in movies_year:
#     print(year.text.strip())
"GENRE"
# movies_genre=doc.find_all('span', class_='genre')
# for genre in movies_genre:
#     print(genre.text.strip())
"DURATION"
# movie_time=doc.find_all('span', class_='runtime')
# for t in movie_time:
#     print(t.text.strip())




"MOVIE DIRECTORS "
# movie_director = doc.find_all('p', class_='text-muted text-small')
# for ele in movie_director:
#     director_tag = ele.find('a')
#     if director_tag:
#         print(director_tag.text)

"MOVIE RATINGS"
# movie_ratings = doc.find_all('span', class_='ipl-rating-star__rating')
# for rating in movie_ratings:
#     if rating.text.strip():  # Check if the rating text exists
#         print(rating.text.strip())


"THE RATINGS"
rating_divs = doc.find_all('div', class_='ipl-rating-star small')


for rating_div in rating_divs:
    rating_span = rating_div.find('span', class_='ipl-rating-star__rating')
    if rating_span:
        rating_value = rating_span.text.strip()
        print(rating_value)
    else:
        print("Rating element not found.")

"MOVIE STARS"
movie_stars = doc.find_all('p', class_='text-muted text-small')
for ele in movie_stars:
    director_tag = ele.find('a')
    if director_tag:
        print(director_tag.text)

print("hhhh")




  

