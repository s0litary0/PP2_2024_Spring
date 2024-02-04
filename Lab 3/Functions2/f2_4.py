from movies import movies

def average_imdb(movies_list):
    ave_score = 0
    counter = 0
    for x in movies_list:
        ave_score += x["imdb"]
        counter += 1
    ave_score = ave_score / counter

    print(ave_score)

average_imdb(movies)