from movies import movies

def category(movies_list, category_name):
    sublist = []
    for x in movies_list:
        if x["category"] == category_name:
            sublist.append(x["name"])

    return sublist

print(category(movies, "Romance"))