from movies import movies

def imdb_5_movies(movies_list):
    sublist = []
    for x in movies_list:
        if x["imdb"] > 5.5:
            sublist.append(x["name"])
    return sublist

print(imdb_5_movies(movies))