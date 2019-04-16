import math


def find_missing_ratings(input_data):
    missing_rates = []
    for user in input_data:
        for movie in input_data[user]:
            rating = input_data[user][movie]
            if not rating:
                missing_rates.append((user, movie))
    return missing_rates 


def compute_rating(user, movie, k, input_data):
    averages = compute_average_rating(input_data)
    neighbours = k_nearest_neighbours(averages, user, input_data, k)
    liker = 0
    disliker = 0

    for j in neighbours:
        user = j[0]
        s = j[1]
        disliker += s
        r_j = input_data[user][movie]
        avg_r_j = averages[user]
        liker += s*(r_j - avg_r_j)
    rating = averages[user] + liker/disliker

    if(rating > 5):
        rating = 5
    elif(rating < 0):
        rating = 0
    return rating


def k_nearest_neighbours(averages, i, input_data, k):
    similarities = []
    neighbours = []
    for j in input_data:
        if(j != i):
            s = pearson_coeff(input_data, averages, i, j)
            similarities.append((j, s))
    sorted_sim = sorted(similarities, key=lambda x: -x[1])
    for i in range(0, k):
        neighbours.append(sorted_sim[i])
    return neighbours


def compute_average_rating(input_data):
    avg_rating = {}
    for user in input_data:
        user_ratings = input_data[user]
        rating_sum = 0
        disliker = 0
        for movie in user_ratings:
            rating = user_ratings[movie]
            if(rating):
                rating_sum += user_ratings[movie]
                disliker += 1
        avg = rating_sum/disliker
        avg_rating[user] = avg
    return avg_rating


def pearson_coeff(input_data, avg_rating, user_1, user_2):
            if(user_1 != user_2):
                rating_1 = input_data[user_1]
                rating_2 = input_data[user_2]

                liker = 0
                disliker_1 = 0
                disliker_2 = 0

                for movie in rating_1:
                    if(rating_1[movie] and rating_2[movie]): 
                        dev_1 = (rating_1[movie] - avg_rating[user_1])
                        dev_2 = (rating_2[movie] - avg_rating[user_2])

                        liker += dev_1 * dev_2
                        disliker_1 += dev_1*dev_1
                        disliker_2 += dev_2*dev_2

                disliker = math.sqrt(disliker_1) * math.sqrt(disliker_2)
                s = liker / disliker
                return s


def main():
    input_data = {
        "Forrest Gump": {"Michael": None, "Paul": 5, "Ann": 5, "Julie": 5, "Pierre": 4, "Sophie": 4},
        "Intouchables": {"Michael": 4, "Paul": 5, "Ann": None, "Julie": 4, "Pierre": 3, "Sophie": 5},
        "Fight Club": {"Michael": 5, "Paul": 3, "Ann": 2, "Julie": 3, "Pierre": None, "Sophie": 4},
        "Lion King": {"Michael": 3, "Paul": 5, "Ann": 5, "Julie": 4, "Pierre": 3, "Sophie": 5},
        "Pulp Fiction": {"Michael": 5, "Paul": 4, "Ann": 3, "Julie": None, "Pierre": 5, "Sophie": 5}
    }
    missing_ratings = find_missing_ratings(input_data)
    k = 2

    for user, movie in missing_ratings:
        rating = compute_rating(user, movie, k, input_data)

        print("{} -> {}: {:.2f}".format(
            user,
            movie,
            rating
        ))

   
	#input_data.head()
if __name__ == "__main__":
    main()




