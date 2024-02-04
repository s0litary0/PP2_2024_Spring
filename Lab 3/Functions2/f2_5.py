from movies import movies

def ave_imdb_by_category(movies_list, category_name):
    ave_score = 0
    counter = 0
    for x in movies_list:
        if x["category"] == category_name:
            ave_score += x["imdb"]
            counter += 1
    ave_score = ave_score / counter
    
    print(ave_score)

ave_imdb_by_category(movies, "Romance")