from movies import movies

def imdb_5(movies_list, movie):
    for x in movies_list:
        if x["name"] == movie:
            return True if x["imdb"] > 5.5 else False

print(imdb_5(movies, "We Two"))