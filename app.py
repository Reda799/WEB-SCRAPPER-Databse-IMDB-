import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the CSV data
df = pd.read_csv('ImdbCSV.csv')  # Replace with the path to your CSV file
root = tk.Tk()
root.title("  Movies")
root.configure(background="#8B0000") 
root.iconbitmap('icon.ico')


title_label = tk.Label(root, text="TOP 100 GREATEST MOVIES  OF ALL TIME ACOORDING TO IMDB", font=("Arial", 24, "bold"), bg="#8B0000", fg="#FFD700")
title_label.pack(fill='x', pady=10)  # Pack it to fill along the x-axis and add some padding at the y-axis for space

# Function to create a frame for each movie's details
def create_movie_frame(container, movie):
    frame = ttk.Frame(container, padding="10", relief="groove")  # Added padding and relief for visual separation
    
    # Title and Year with better alignment
    title_label = ttk.Label(frame, text=f"{movie['Name Of Movie']} ({movie['Release Year']})", font=("Arial", 16, "bold"))
    title_label.grid(row=0, column=0, sticky="W")

    # Rating
    rating_label = ttk.Label(frame, text=f"Rating: {movie['Ratings']} |  Runtime: {movie['Duration In Minutes']} min", font=("Arial", 12))
    rating_label.grid(row=1, column=0, sticky="W")
    rating_label.config(foreground="blue")

    # Votes and Gross in a more compact form
    votes_gross_label = ttk.Label(frame, text=f"Votes: {movie['Votes'] } | Genre: {movie['Genre']} | Gross: {movie['Gross Earnings']}", font=("Arial", 12))
    votes_gross_label.grid(row=2, column=0, sticky="W")

    # Oscars with conditional highlighting
    oscars_text = f"Oscars Won: {movie['Oscars Won']} | Oscar Nominations: {movie['Oscar Nominations']}"
    oscars_label = ttk.Label(frame, text=oscars_text, font=("Arial", 12, "italic"))
    
    oscars_label.config(foreground="red")  # Highlight if Oscars are won
    oscars_label.grid(row=3, column=0, sticky="W")

    return frame
def update_display(sorted_movies):
    # Clear existing frames
    for child in scrollable_frame.winfo_children():
        child.destroy()
    for movie in sorted_movies:
        movie_frame = create_movie_frame(scrollable_frame, movie)
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
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'))
    elif criterion == 'Newest':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'), reverse=True)
    elif criterion == 'Alphabetic Order':
        sorted_movies = sorted(movies_data, key=lambda x: x['Name Of Movie'].upper())  # Use upper() for case-insensitive sort
    elif criterion == 'Ratings':
        sorted_movies = sorted(movies_data, key=lambda x: x['Ratings'], reverse=True)
    elif criterion == 'Most Gross Income':
        sorted_movies = sorted(movies_data, key=lambda x: convert_gross(x['Gross Earnings']), reverse=True)
    elif criterion == 'Most Oscars Won':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Oscars Won'), reverse=True)
    elif criterion == 'Most Oscar Nominations':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Oscar Nominations'), reverse=True)



    update_display(sorted_movies)
   
    update_display(sorted_movies)




# Create the main application window


# Create a scrollable canvas
canvas = tk.Canvas(root)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Load the movie data

# Create a combobox for sorting options
sort_options = ['Oldest', 'Newest','Ratings','Most Gross Income', 'Most Oscars Won', 'Most Oscar Nominations']
sort_combobox = ttk.Combobox(root, values=sort_options, state='readonly')
sort_combobox.pack(fill='x', padx=10, pady=5)
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
