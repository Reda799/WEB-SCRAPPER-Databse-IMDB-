
import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.imdb.com/list/ls055592025/')
page_contents = r.text
doc = BeautifulSoup(page_contents, 'html.parser')

Name = []
Year = []
Genre = []
Time = []
Ratings = []
Votes = []
Gross = []
OscarNominations = []
OscarsWon = []

movie_data = doc.find_all('div', attrs={'class': 'lister-item mode-detail'})
for i in movie_data:
    
    name = i.h3.a.text
    Name.append(name)

    movie_year = i.find('span', class_='lister-item-year text-muted unbold').get_text(strip=True)
    Year.append(movie_year)

    movies_genre = i.find('span', class_='genre').get_text(strip=True)
    Genre.append(movies_genre)

    movie_time = i.find('span', class_='runtime').get_text(strip=True).replace('min', '')
    Time.append(int(movie_time))

    rating = i.find('div', class_='ipl-rating-star small').get_text(strip=True)
    Ratings.append(float(rating))

    value = i.findAll('span', attrs={'name': 'nv'})
    vote = value[0].text
    Votes.append(vote)
    grosses = value[1].text if len(value) > 1 else 'NO Information '
    Gross.append(grosses)

    # Extracting Oscar Nominations
    prize_info = i.find('div', class_='list-description').get_text(strip=True)
    prize_lines = prize_info.split('\n')
    for line in prize_lines:
        if "Oscar Nominations" in line:
            nominations = int(line.split(':')[1].strip())
            OscarNominations.append(nominations)
            break
    else:
        OscarNominations.append(None)
    # Extracting Oscar winns
    for line in prize_lines:
        if "Oscars" in line:
            won = int(line.split(':')[2].strip())
            OscarsWon.append(won)
            break
    else:
        OscarsWon.append(None)
    
# print(OscarsWon)        
# Extract the year from the 'Release Year' string
import re 
def extract_year(year_str):
    year = year_str.strip("()")
    # Match only the first four digits (the year)
    match = re.search(r'\b(19|20)\d{2}\b', year)
    if match:
        return int(match.group(0))
    return None  # If no valid year is found, return None

# Clean the 'Year' list using the function defined above
cleaned_years = [extract_year(y) for y in Year]
Year = cleaned_years

movie_DF = pd.DataFrame({'Name Of Movie': Name, 'Release Year': Year, 'Genre': Genre, 'Duration In Minutes': Time,
                         'Ratings': Ratings, 'Votes': Votes, 'Gross Earnings': Gross,
                         'Oscar Nominations': OscarNominations, 'Oscars Won': OscarsWon})
# print(movie_DF)
 
movie_DF['Oscar Nominations'].fillna(0, inplace=True)
movie_DF['Oscars Won'].fillna(0, inplace=True)

movie_DF.to_csv("ImdbCSV.csv")
