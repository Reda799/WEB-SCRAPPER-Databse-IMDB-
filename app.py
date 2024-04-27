import tkinter as tk
from tkinter import ttk
import pandas as pd

# Load the CSV data
df = pd.read_csv('ImdbCSV2.csv')  # Replace with the path to your CSV file

# Function to create a frame for each movie's details
def create_movie_frame(container, movie):
    frame = ttk.Frame(container)
    
    # Title and Year
    title_label = ttk.Label(frame, text=f"{movie['Name Of Movie']} {movie['Release Year']}", font=("Arial", 18, "bold"))
    title_label.grid(row=0, column=0, sticky="W", pady=5)

    # Rating
    rating_label = ttk.Label(frame, text=f"Rating: {movie['Ratings']} | Run Time(in Minutes): {movie['Duration In Minutes']}")
    rating_label.grid(row=1, column=0, sticky="W")

    # Votes and Gross
    votes_gross_label = ttk.Label(frame, text=f"Votes: {movie['Votes']} | Gross: {movie['Gross Earnings']}")
    votes_gross_label.grid(row=2, column=0, sticky="W")

    # Oscars
    oscars_label = ttk.Label(frame, text=f"Oscars: {movie['Oscars Won']} | Oscar Nominations: {movie['Oscar Nominations']}")
    oscars_label.grid(row=3, column=0, sticky="W")
    
    # Add padding to the frame and return it
    for child in frame.winfo_children():
        child.grid_configure(padx=8, pady=2)
    
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
    

    if criterion == 'Oldest':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'))
    elif criterion == 'Newest':
        sorted_movies = sorted(movies_data, key=lambda x: get_value(x, 'Release Year'), reverse=True)
    elif criterion == 'Alphabetic Order':
        sorted_movies = sorted(movies_data, key=lambda x: x['Name Of Movie'].upper())  # Use upper() for case-insensitive sort
    elif criterion == 'Ratings':
        sorted_movies = sorted(movies_data, key=lambda x: x['Ratings'], reverse=True)

    update_display(sorted_movies)
   
    update_display(sorted_movies)




# Create the main application window
root = tk.Tk()
root.title("Movie Details")

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
movies_data = df.to_dict(orient="records")

# Create a combobox for sorting options
sort_options = ['Oldest', 'Newest']
sort_combobox = ttk.Combobox(root, values=sort_options, state='readonly')
sort_combobox.pack(fill='x', padx=10, pady=5)
sort_combobox.set('Sort by')
sort_combobox.bind('<<ComboboxSelected>>', lambda event: sort_movies(sort_combobox.get()))


# Iterate over the movies and create a frame for each
for movie in movies_data:
    movie_frame = create_movie_frame(scrollable_frame, movie)
    movie_frame.pack(fill='x', expand=True, pady=10)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Run the application
root.mainloop()
