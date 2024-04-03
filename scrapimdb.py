import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

r = requests.get('https://www.imdb.com/list/ls055592025/')
page_contents = r.text
doc = BeautifulSoup(page_contents, 'html.parser')


Name=[]
Year=[]
Genre=[]
Time=[]
Ratings=[]
Stars=[]
Gross=[]
Votes=[]
OscarNominations=[]
Prizes=[]
OscarsWon=[]
# movie_data=doc.find_all('div',attrs={'class':'lister-item mode-detail'})




"MOVIE NAMES "
# movie_names = doc.find_all('h3', class_='lister-item-header')
# for ele in movie_names:
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


# for p_tag in p_tags:
#     if 'Stars:' in p_tag.text:
#         stars_links = p_tag.find_all('a', href=lambda x: x and '/name/' in x)
#         stars = [star.text for star in stars_links]
#         stars = stars[1:]
#         print(stars)


"Gross earnings"
   
# span_elements = doc.find_all('span', {'name': 'nv', 'data-value': True})
    
# for span_element in span_elements:
#         text_content = span_element.text
        
#         if text_content.endswith("M"):
#             print("Gross:", text_content)






"MOVIES WITH MORE THEN ONE DIRECTOR "       
# p_tags = doc.find_all('p', class_='text-muted text-small')

# for p_tag in p_tags:
#     if ('Directors:')    in p_tag.text:
#         director_links = p_tag.find_all('a', href=lambda x: x and '/name/' in x)
#         directors = [director.text for director in director_links]
#         print(directors[:-4])
          


movie_data = doc.find_all('div', attrs={'class': 'lister-item mode-detail'})
for i in movie_data:
    name=i.h3.a.text
    Name.append(name)
# print(Name)
    movie_year = i.find('span', class_='lister-item-year text-muted unbold').get_text(strip=True)
    Year.append(movie_year)

# print(years)
    movies_genre=i.find('span', class_='genre').get_text(strip=True)
    Genre.append(movies_genre)
# print(Genre)    
    movie_time=i.find('span', class_='runtime').get_text(strip=True).replace('min','')
    Time = [int(item) for item in Time]# convert to integers 
    Time.append(movie_time)
# print(Time)  
    rating=i.find('div', class_='ipl-rating-star small').get_text(strip=True)
    Ratings = [float(item) for item in Ratings]
    Ratings.append(rating) 
# print(Ratings)
### GROSS SECTION
    value=i.findAll('span',attrs={'name':'nv'})
    vote=value[0].text
    Votes.append(vote)
    grosses=value[1].text if len(value)>1 else '*****'
    Gross.append(grosses)
# Prizes^
    prize_info = i.find('div', class_='list-description').get_text(strip=True)
    prize_lines = prize_info.split('\n')
    for line in prize_lines:
        if "Oscar Nominations" in line:
            nominations = int(line.split(':')[1].strip())
            OscarNominations.append(nominations)
            break
    else:
        OscarNominations.append(None)
# print(OscarNominations)        
    
    
    
    

   

  


movie_DF=pd.DataFrame({'Name Of Movie':Name , 'Release Year':Year,'Genre':Genre,'Duration In Minutes':Time,'Ratings':Ratings,'Votes':Votes,'Gross Earnings':Gross,'Oscar Nominations':OscarNominations})    

# print(movie_DF)


