# Assignment 2: Movie Database

movies = [
{"id":1,"name":"Inception","rating":8.8,"year":2010},
{"id":2,"name":"Avatar","rating":7.8,"year":2009},
{"id":3,"name":"Interstellar","rating":8.7,"year":2014},
{"id":4,"name":"Dune","rating":8.1,"year":2021},
{"id":5,"name":"Tenet","rating":7.4,"year":2020}
]

# Tasks
# Find movies released after 2015 .XXX

print("Movies after 2015: ")
# for movi in movies:
#     if movi['year'] > 2015:
#         print(movi.get('name'))

# movies_2015 = list(filter(lambda x : x["year"] > 2015, movies))
# print(movies_2015, sep="\n")

def find_2015_movies(x : dict):
    return x.get("name") and x.get("year") if x.get("year") > 2015 else None

movies_2015 = list(filter(find_2015_movies, movies))
print(movies_2015, sep="\n")

# Find the highest-rated movie.

print("\nHighest rated movie is: ")

# def max_rating(x):
#     if x.get('rating') == max(movies, key= lambda y : y['rating']).get('rating'):
#         return x['name'], x['rating'] #return touple
#     return None

# for mov in movies:
#     if(max_rating(mov)):
#         ans = max_rating(mov)
#         if ans: 
#             print(ans[0], ans[1])
        

sorted_rating = sorted(movies, key=lambda x: x['rating'], reverse=True)
print(sorted_rating[0].get('name'), sorted_rating[0]['rating'])

# max_rating_movie = list(filter(max_rating, movies))
# print(max_rating_movie)

# highest_rating = max(movies, key = lambda x: x['rating'])
# print(highest_rating['name'])




# Find the second highest-rated movie.

print("\nSecond highest rating Movie is: ")

print(sorted_rating[1].get('name'), sorted_rating[1]['rating'])



# # Sort by rating.

# def sort_rating(itemObj: dict):
#     return itemObj.get("rating")

# sorted_byRating = sorted(movies, key = sort_rating)
# print("Sorted by Price: ",sorted_byRating)

sorted_byRating = sorted(movies, key = lambda x: x['rating'])
print("\nSorted by Price: ",sorted_byRating)



# Sort by release year.

sorted_byYear = sorted(movies, key = lambda x: x['year'])
print("\nSorted by Year: ",sorted_byYear)



# Calculate average rating.

print("\nAverage rating is: ")
avg_rating = sum(m['rating'] for m in movies)/ len(movies)
print(avg_rating)



# Find movies whose names end with 'o'.

print("movies whose names end with 'o': ")

def ending_withO(mov):
    if mov['name'].lower().endswith('o') == 'o':
        return mov['name']
    return None
    
movie_list = list(filter(ending_withO, movies))
print(movie_list)



# Count movies with rating above 8

cnt_rating = sum(1 for m in movies if m['rating'] > 8)
print("\nmovies with rating above 8: ", cnt_rating)