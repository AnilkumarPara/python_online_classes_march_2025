"""
WAP to find a movie names starts with 'G' in the given list of movies
using for loop
"""
movies = ("Star wars", "Gundamma katha", "Gadar", "Gadzilla", "Robo")
movies_starts_g = []
for movie in movies:
    if movie.startswith('G'):
        movies_starts_g.append(movie)
print(movies_starts_g)
