Movie Recommendation System using Netflix Movie Ratings

This project involves building a movie recommendation system utilizing Netflix movie ratings. The dataset consists of 17,337,458 ratings given by 143,458 users to 1,350 movies. Ratings range from 1 to 5.

Table of Contents
Load Rating Data
Load Movie Data
Analyze Data
Recommendation Model
4.1 Collaborative Filtering - SVD
1. Load Rating Data
The rating data is loaded from the 'Netflix_Dataset_Rating.csv' file. It contains information about user ratings for various movies.

2. Load Movie Data
Movie data is loaded from the 'Netflix_Dataset_Movie.csv' file. This dataset includes details about the movies such as title, year, and genre.

3. Analyze Data
Data analysis is performed on the rating data to gain insights into the number of ratings per user and per movie. Movie filtering is applied to eliminate movies with insufficient ratings, and a movie summary is generated.

4. Recommendation Model
4.1 Collaborative Filtering - SVD
A Singular Value Decomposition (SVD) collaborative filtering model is implemented using the Surprise library. The data is split into training and testing sets, and the SVD model is trained on the training set. Predictions are then made on the test set, and the Root Mean Squared Error (RMSE) is calculated to evaluate the model's performance.

Usage Example
To demonstrate the recommendation system, two users (712664 and 2643029) are provided as examples. The Recommendation function is used to generate movie recommendations for these users based on their preferences.

python
Copy code
# Movie Recommendation for User - 712664
Recommendation(712664, 10)

# Movie Recommendation for User - 2643029
Recommendation(2643029, 5)
These functions output a DataFrame with movie recommendations sorted by estimated rating in descending order.

Dependencies
Ensure you have the necessary libraries installed before running the code. You can install the required library using the following:

python
Copy code
!pip install scikit-surprise
Dataset
The dataset used for this project includes two CSV files: 'Netflix_Dataset_Rating.csv' and 'Netflix_Dataset_Movie.csv'. The rating file contains user ratings, and the movie file contains information about each movie.

Notes
This code assumes that the required datasets are present in the same directory as the script.
Make sure to adjust file paths and dependencies according to your environment.
Feel free to customize and extend the code for your specific use case or dataset.