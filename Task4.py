import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data
data = pd.read_csv('user_movie_rating_csv.csv')

# Display sample data
print("Sample data:")
print(data.head())

# Create user-movie matrix
um_matrix = data.pivot(index='User', columns='Movie', values='Rating').fillna(0)

# Compute user similarity matrix
user_sim = cosine_similarity(um_matrix)
user_sim_data = pd.DataFrame(user_sim, index=um_matrix.index, columns=um_matrix.index)

# Compute movie similarity matrix
movie_sim = cosine_similarity(um_matrix.T)
movie_sim_data = pd.DataFrame(movie_sim, index=um_matrix.columns, columns=um_matrix.columns)

def recommend_movies(user, num_rec, method='user'):
    """
    Recommend movies to a user based on collaborative filtering.

    Args:
        user (str): Username of the target user.
        num_rec (int): Number of recommendations to generate.
        method (str): Recommendation method ('user' or 'item').

    Returns:
        list or str: List of recommended movies or error message.
    """
    user = user.lower()
    
    if user not in um_matrix.index:
        return "User not found."
    
    if method == 'user':
        # User-based collaborative filtering
        user_rating = um_matrix.loc[user]
        sim_users = user_sim_data[user].sort_values(ascending=False)[1:]
        recommendation = {}

        for sim_user, sim_score in sim_users.items():
            sim_user_rating = um_matrix.loc[sim_user]
            for movie, rating in sim_user_rating.items():
                if user_rating[movie] == 0 and movie not in recommendation:
                    recommendation[movie] = sim_score * rating

    elif method == 'item':
        # Item-based collaborative filtering
        user_rating = um_matrix.loc[user]
        recommendation = {}

        for movie, rating in user_rating.items():
            if rating > 0:
                similar_movies = movie_sim_data[movie].sort_values(ascending=False)[1:]
                for sim_movie, sim_score in similar_movies.items():
                    if user_rating[sim_movie] == 0 and sim_movie not in recommendation:
                        recommendation[sim_movie] = sim_score * rating
    else:
        return "Invalid recommendation method. Choose 'user' or 'item'."
    
    # Sort and return top recommendations
    recommend_movies = sorted(recommendation.items(), key=lambda x: x[1], reverse=True)[:num_rec]
    return recommend_movies

# Main program
print("\nWelcome to the Movie Recommendation System!")
uname = input("Enter your username: ").lower()
num_rec = int(input("Enter the number of movies to recommend: "))
method = input("Choose recommendation method ('user' or 'item'): ").lower()

recommendation = recommend_movies(uname, num_rec, method)

print(f"\nRecommendations for {uname} using {method}-based filtering:")
if isinstance(recommendation, str):
    print(recommendation)
else:
    for movie, score in recommendation:
        print(f"{movie} (Predicted Score: {score:.2f})")