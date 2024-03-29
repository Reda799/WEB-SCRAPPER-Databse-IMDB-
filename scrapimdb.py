import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.imdb.com/list/ls055592025/')
page_contents = r.text
doc = BeautifulSoup(page_contents, 'html.parser')
"MOVIE NAMES "
# movie_names = doc.find_all('h3', class_='lister-item-header')
# for ele in movie_names:
#  print(ele.find('a').text)


"YEAR "
# movies_year = doc.find_all('span', class_='lister-item-year text-muted unbold')
# for year in movies_year:
#     print(year.text.strip())
# "GENRE"
# movies_genre=doc.find_all('span', class_='genre')
# for genre in movies_genre:
#     print(genre.text.strip())
# "DURATION"
# movie_time=doc.find_all('span', class_='runtime')
# for t in movie_time:
#     print(t.text.strip())






"THE RATINGS"
# rating_divs = doc.find_all('div', class_='ipl-rating-star small')


# for rating_div in rating_divs:
#     rating_span = rating_div.find('span', class_='ipl-rating-star__rating')
#     if rating_span:
#         rating_value = rating_span.text.strip()
#         print(rating_value)
#     else:
#         print("Rating element not found.")

"MOVIE STARS"
# p_tags = doc.find_all('p', class_='text-muted text-small')

# Print the actor names

# for p_tag in p_tags:
#     if 'Stars:' in p_tag.text:
#         stars_links = p_tag.find_all('a', href=lambda x: x and '/name/' in x)
#         stars = [star.text for star in stars_links]
#         stars = stars[1:]
#         print(stars)

"MOVIES WITH ONE DIRECTOR"
# movie_director = doc.find_all('p', class_='text-muted text-small')
# for ele in movie_director:
#     director_tag = ele.find('a')
#     if director_tag:
#         print(director_tag.text)

 
   
#  print(ele.find('p').text)
 
#  print("item finished")

"Gross earnings"
# span_elements = doc.find_all('span', {'name': 'nv', 'data-value': True})
    

    
# span_elements = doc.find_all('span', {'name': 'nv', 'data-value': True})
    
# for span_element in span_elements:
#         text_content = span_element.text
        
#         if text_content.endswith("M"):
#             print("Text Content:", text_content)


# p_tags = doc.find_all('p', class_='text-muted text-small')



"MOVIES WITH MORE THEN ONE DIRECTOR "       
p_tags = doc.find_all('p', class_='text-muted text-small')

for p_tag in p_tags:
    if ('Directors:')    in p_tag.text:
        director_links = p_tag.find_all('a', href=lambda x: x and '/name/' in x)
        directors = [director.text for director in director_links]
        print(directors[:-4])
          # Stop searching after finding directors

