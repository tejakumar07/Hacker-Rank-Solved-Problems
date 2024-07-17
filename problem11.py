movies = [
    "Baahubali: The Beginning",
    "Baahubali 2: The Conclusion",
    "Arjun Reddy",
    "Jersey",
    "Ala Vaikunthapurramuloo",
    "Rangasthalam",
    "Bharat Ane Nenu",
    "Mirchi",
    "Khaleja",
    "Eega",
    "Manam",
    "Maharshi",
    "Srimanthudu",
    "Pokiri",
    "Magadheera",
    "Attarintiki Daredi",
    "Gharshana",
    "Leader",
    "Yevadu",
    "Nuvvu Naaku Nachav",
    "Arya",
    "Gabbar Singh",
    "Hello",
    "Bommarillu",
    "Happy Days",
    "Athadu",
    "Amar Akbar Anthony",
    "Fidaa",
    "Geetha Govindam",
    "Awe!"
]


smovies = []

for title in movies:
    if title.startswith("S"):
        smovies.append(title)


print(smovies)

#This can be executed in single line also

bmovies = [title for title in movies if title.startswith("B")]

print(bmovies)