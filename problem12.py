movies = [
    ("Inception", 2010),
    ("The Matrix", 1999),
    ("Pulp Fiction", 1994),
    ("The Shawshank Redemption", 1994),
    ("The Dark Knight", 2008),
    ("Forrest Gump", 1994),
    ("Interstellar", 2014),
    ("Fight Club", 1999),
    ("The Lord of the Rings: The Fellowship of the Ring", 2001),
    ("Gladiator", 2000)
]

mov =[titles for (titles,year) in movies if year > 2000]

print(mov)