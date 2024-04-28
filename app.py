import tkinter as tk
from tkinter import ttk
import pandas as pd
# Load the CSV data
df = pd.read_csv('ImdbCSV.csv') 
# Test if the csvfile is not empty and that 
assert not df.empty, "Dataframe is empty. Check the CSV file path and content."
# Initialize the main window of the application
root = tk.Tk()
root.title("  Movies")
root.configure(background="#8B0000") # Set background color for the window
root.iconbitmap('icon.ico') # put an icon for the window

# Create a title label on top of the window
title_label = tk.Label(root, text="TOP 100 GREATEST MOVIES  OF ALL TIME ACOORDING TO IMDB", font=("Arial", 24, "bold"), bg="#8B0000", fg="#FFD700")
title_label.pack(fill='x', pady=10)  

# Function to create a frame for each movie's details
def create_movie_frame(container, movie):
    frame = ttk.Frame(container, padding="10", relief="groove") # A frame that contains all the movie details
    # Create and grid a label for the movie's name and release year
    title_label = ttk.Label(frame, text=f"{movie['Name Of Movie']} ({movie['Release Year']})", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, sticky="W")

     #movie's rating and run time
    rating_label = ttk.Label(frame, text=f"Rating: {movie['Ratings']} |  Runtime: {movie['Duration In Minutes']} min", font=("Arial", 12))
    rating_label.grid(row=1, column=0, sticky="W")
    rating_label.config(foreground="blue")

    # Votes, genre and gross income of the movie
    votes_gross_label = ttk.Label(frame, text=f"Votes: {movie['Votes'] } | Genre: {movie['Genre']} | Gross: {movie['Gross Earnings']}", font=("Arial", 12))
    votes_gross_label.grid(row=2, column=0, sticky="W")

    # Oscars and nominations
    oscars_text = f"Oscars Won: {movie['Oscars Won']} | Oscar Nominations: {movie['Oscar Nominations']}"
    oscars_label = ttk.Label(frame, text=oscars_text, font=("Arial", 12, "italic"))
    # coloring with red
    oscars_label.config(foreground="red")  
    oscars_label.grid(row=3, column=0, sticky="W")
    # Test that the movie frame contains all the required labels
    assert title_label.winfo_exists(), "Title label does not exist in the movie frame."
    assert rating_label.winfo_exists(), "Rating label does not exist in the movie frame."
    assert votes_gross_label.winfo_exists(), "Votes/Gross label does not exist in the movie frame."
    assert oscars_label.winfo_exists(), "Oscars label does not exist in the movie frame."

    return frame
 #function to update the display with sorted movie frames
def update_display(sorted_movies):
    # Clear existing frames
    for child in scrollable_frame.winfo_children():
        child.destroy() # destroy and clear all present movie frames before updating
    for movie in sorted_movies:
        movie_frame = create_movie_frame(scrollable_frame, movie)  # Create a frame for each sorted movie
        movie_frame.pack(fill='x', expand=True, pady=10)

def sort_movies(criterion):
    def get_value(movie, key):
        try:
            # Assuming numeric values for Oscars and Year, replace empty strings with 0 or a very old year
            return int(movie[key]) if key != 'Name Of Movie' else movie[key]
        except ValueError:
            return 0 if key in ['Oscars Won', 'Oscar Nominations'] else "A very old year"
    def convert_gross(gross_str):
        if gross_str.startswith('$') and gross_str.endswith('M'):
            return float(gross_str[1:-1]) * 1_000_000
        elif gross_str.startswith('$') and gross_str.endswith('K'):
            return float(gross_str[1:-1]) * 1_000
        return 0

    

    if criterion == 'Oldest':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'))# sort by realse year from oldest to newest
    elif criterion == 'Newest':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'), reverse=True) # sort by realse year from newest to oldest
    elif criterion == 'Alphabetic Order':
        sorted_movies = sorted(movies_data, key=lambda x: x['Name Of Movie'].upper()) #sort by alphabetic order
    elif criterion == 'Ratings':
         sorted_movies = sorted(movies_data, key=lambda x: x['Ratings'], reverse=True) # sort by ratings from biggest to lowest 
    elif criterion == 'Most Gross Income':
        sorted_movies = sorted(movies_data, key=lambda x: convert_gross(x['Gross Earnings']), reverse=True) # sort by gross income
    elif criterion == 'Most Oscars Won':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Oscars Won'), reverse=True) # sort by the number oscars
    elif criterion == 'Most Oscar Nominations':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Oscar Nominations'), reverse=True) # sort by the number of oscar nominations



    update_display(sorted_movies)  # Call the update_display function with sorted movies

   
   







# Create a canvas and scrollbar for the scrollable movie list
canvas = tk.Canvas(root)
#Make a Scrollbar widget and configure it to respond to the canvas view by scrolling vertically.
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
#build a fram that will include each movie gframe
scrollable_frame = ttk.Frame(canvas)
# Bind the configure event of the scrollable frame to adjust the scrolling area in the canvas
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
# Configure the canvas to respond to the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)



# Create a combobox for sorting options
sort_options = ['Oldest', 'Newest','Alphabetic Order','Ratings','Most Gross Income', 'Most Oscars Won', 'Most Oscar Nominations']
# Initialize the combobox with the sorting options defined above and set its state to 'readonly'
sort_combobox = ttk.Combobox(root, values=sort_options, state='readonly')
#Fill the upper portion of the window with the combobox, leaving space for padding on the x and y axes.
sort_combobox.pack(fill='x', padx=10, pady=5)
# Put the default text of the combobox
sort_combobox.set('Sort by')
sort_combobox.bind('<<ComboboxSelected>>', lambda event: sort_movies(sort_combobox.get()))
# Load the movie data
movies_data = df.to_dict(orient="records")



# Iterate over the movies and create a frame for each
for movie in movies_data:
    movie_frame = create_movie_frame(scrollable_frame, movie)
    movie_frame.pack(fill='x', expand=True, pady=10)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the application

root.mainloop()
   