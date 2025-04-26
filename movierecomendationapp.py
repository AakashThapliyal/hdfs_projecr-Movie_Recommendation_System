import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button
import requests
import subprocess

API_KEY = "b03e2fb1bc28d83575f669db160fed82"
recommended_movies = []

def get_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    response = requests.get(url)
    data = response.json()
    results = data.get("results")
    if results:
        return results[0]["id"]
    return None

def get_movie_genres(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    genres = data.get("genres", [])
    return [genre["id"] for genre in genres]

def get_similar_movies(genre_ids):
    genre_str = ",".join(map(str, genre_ids))
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_str}&sort_by=popularity.desc"
    response = requests.get(url)
    data = response.json()
    movies = [movie["title"] for movie in data.get("results", [])][:5]
    return movies

def save_to_hdfs():
    if not recommended_movies:
        messagebox.showwarning("No Recommendations", "Please generate recommendations first.")
        return
    try:
        # Save locally
        with open("recommendations.txt", "w") as f:
            for movie in recommended_movies:
                f.write(movie + "\n")

        # Upload to HDFS
        result = subprocess.run(["hdfs", "dfs", "-put", "-f", "recommendations.txt", "/movie/input/"], capture_output=True, text=True)
        if result.returncode != 0:
            raise Exception(result.stderr)

        messagebox.showinfo("Success", "Saved to HDFS at /movie/input/recommendations.txt")
    except Exception as e:
        messagebox.showerror("HDFS Error", f"Could not save to HDFS:\n{e}")

def show_popup(similar_movies):
    popup = Toplevel(window)
    popup.title("Recommendations")
    popup.geometry("400x250")
    popup.configure(bg="#282a36")

    label = Label(popup, text="💡 Movies you might like:", font=("Helvetica", 12, "bold"), fg="#f8f8f2", bg="#282a36")
    label.pack(pady=10)

    for movie in similar_movies:
        Label(popup, text=movie, font=("Helvetica", 10), fg="#f1fa8c", bg="#282a36").pack()

    save_btn = Button(popup, text="💾 Save to HDFS", font=("Helvetica", 11), bg="#8be9fd", command=save_to_hdfs)
    save_btn.pack(pady=15)

    Button(popup, text="OK", font=("Helvetica", 10), command=popup.destroy).pack()

def recommend():
    global recommended_movies
    movie_name = entry.get()
    if not movie_name:
        messagebox.showwarning("Input Error", "Please enter a movie name.")
        return

    movie_id = get_movie_id(movie_name)
    if not movie_id:
        messagebox.showerror("Error", "Movie not found.")
        return

    genres = get_movie_genres(movie_id)
    if not genres:
        messagebox.showerror("Error", "Genres not found.")
        return

    recommended_movies = get_similar_movies(genres)
    if recommended_movies:
        show_popup(recommended_movies)
    else:
        messagebox.showinfo("No Results", "No similar movies found.")

# GUI setup
window = tk.Tk()
window.title("🎬 Movie Recommender")
window.geometry("500x300")
window.configure(bg="#1e1e2e")

title_label = tk.Label(window, text="🎥 Movie Recommendation System", font=("Helvetica", 16, "bold"), fg="#f1fa8c", bg="#1e1e2e")
title_label.pack(pady=15)

instruction_label = tk.Label(window, text="Type the name of a movie you like (e.g., Inception, Titanic, Avatar):", font=("Helvetica", 10), fg="#f8f8f2", bg="#1e1e2e")
instruction_label.pack()

entry = tk.Entry(window, font=("Helvetica", 12), width=40, justify="center")
entry.pack(pady=10)

btn = tk.Button(window, text="🎯 Recommend Movies", font=("Helvetica", 12), bg="#50fa7b", fg="black", command=recommend)
btn.pack(pady=15)

footer = tk.Label(window, text="by Aakash and Aditya", font=("Helvetica", 9), fg="#6272a4", bg="#1e1e2e")
footer.pack(side="bottom", pady=10)

window.mainloop()
