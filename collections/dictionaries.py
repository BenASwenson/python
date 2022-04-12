# Dictionaries

# key-value pairs

me = {
    "name": "David",
    "job": "Trainer",
    "age": 31
}

# print(me, type(me))

# # DICTIONARY NAME [ KEY ]
# print(me['name'])
# me['name'] = 'Ben'
# print(me['name'])
# me['hobbies'] = ['snowmobiling', 'snowboarding', 'skating', 'guitar']
#
# me['job'] = 'student'
# me['age'] = 45
# print(me.get('name'))
# me.update({'name': 'B. A. Swenson'})
# print(me)

# Make a dictionary with information about your favourite film

favourite_film = {
    "title": "The Godfather",
    "director": "Francis Ford Coppola",
    "writers": ("Mario Puzo", "Francis Ford Coppola"),
    "stars": ("Marlon Brando", "Al Pacino", "James Caan"),
    "year": 1972
}

print(favourite_film.keys())
print(favourite_film.values())
print(favourite_film.items())

