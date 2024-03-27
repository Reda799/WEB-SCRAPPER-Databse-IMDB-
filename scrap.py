import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/list/ls055592025/')
page_contents = r.text
doc = BeautifulSoup(page_contents, 'html.parser')

movie_names = doc.find_all('h3', class_='lister-item-header')
for ele in movie_names:
    # Find the 'a' tag within the 'h3' tag and then access its text
    print(ele.find('a').text)

print("HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

movies_year = doc.find_all('span', class_='lister-item-year text-muted unbold')
for year in movies_year:
    print(year.text.strip())


 

