I confirm that this assignment is my own work.    
Where I have referred to academic sources, I have provided in-text citations and included the sources in the final reference list.   

KAPLAN INTERNATIONAL COLLEGE LONDON – IYO COMPUTER SCIENCE PROGRAMME  
Module Title: INTRO T PROGRAMMING
Pnumber:  P440014 
Name: REDA GHARDI  
Description of the Program:
This programme includes a data file called ImdbCSV.csv and two Python scripts called app.py and scrapimdb.py. IMDb information such as movie titles, release dates, genres, reviews, votes, gross earnings, Oscar nominations, and wins can be scraped using the scrapimdb.py script. After that, it cleans and organises the data before saving it in a CSV file called ImdbCSV.csv.

This CSV file is used by the app.py script, which uses Tkinter, a Python desktop application toolkit, to generate a graphical user interface (GUI). With information on movie titles, ratings, runtime, genres, and Oscar-related features, the application displays a list of the best films based on data from IMDb. Users are able to access extensive movie data in an aesthetically pleasing style thanks to this intuitive interface.

Usage:
Movie buffs or scholars who want to examine IMDb movie data without having to browse the website manually can use the programme. Users can automatically gather and refresh their database with the most recent IMDb data by executing the scrapimdb.py script. The GUI may then be launched by running the app.py script, making it simple to work with the data. For fast lookups, data visualisations, or even teaching reasons, this might be extremely helpful for examining changes in movie ratings and success metrics over time. The application allows users to study specifics about each film, which makes it a great tool for learning about trends and accomplishments in the film industry.

All libraries/Packages Used:
tkinter: Used for creating the GUI elements in the application.
ttk (from tkinter): Provides access to themed widgets that enhance the appearance of the application.

Installation Instructions:
1.Install Python
2.Install Required Libraries
Open a terminal or command prompt and install the necessary Python libraries by executing:
pip install pandas
pip install requests
pip install beautifulsoup4
3.Prepare the Environment
Place the script files (app.py and scrapimdb.py) and the data file (ImdbCSV.csv) in the same directory.

Instructions on How to Run the Program:
1.Run the Web Scraping Script:
To begin scraping and processing the IMDb data, navigate to the directory holding the script files and run scrapimdb.py:
python scrapimdb.py
This script fetches the latest movie data from IMDb and saves it to ImdbCSV.csv.
2.Launch the GUI Application:
Once the data is prepared, start the GUI application by running:
python app.py
This launches the graphical user interface (GUI), which presents the movie data in an approachable manner for interaction and exploration of different cinematic insights.
pandas: Used for loading, manipulating, and displaying data from the ImdbCSV.csv file.

requests: Allows sending HTTP requests to fetch web pages for scraping.
bs4 (BeautifulSoup): Used for parsing HTML and XML documents, making it easier to scrape data.
pandas:used to arrange the data that has been scraped by constructing and modifying data structures.
re (regex): used to carry out tasks using regular expressions, including pattern extraction from text.
