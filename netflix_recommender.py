# Movie Recommendation using Netflix Movie Reviews

This project aims to build a movie recommendation system using Netflix Movie Ratings. There are 17337458 Ratings given by 143458 users to 1350 movies. Ratings are in the form of Integer i.e. 1 - 5

**Table of Content**

#### 1.  Load Rating Data
#### 2.  Load Movie Data
#### 3.  Analyze Data
#### 4.  Recommendation Model
#### 4.1 Collaborative Filtering - SVD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

! pip install scikit-surprise

from surprise import Reader, Dataset, SVD
from surprise import accuracy
from surprise.model_selection import train_test_split

"""# 1. Load Rating Data"""

df = pd.read_csv('Netflix_Dataset_Rating.csv')
df

df.dtypes

df.info()

df['Rating'].describe().astype('int')

print("Unique Values :\n",df.nunique())

"""# 2. Load Movie Data"""

df_title = pd.read_csv('Netflix_Dataset_Movie.csv')
df_title

df_title.dtypes

df_title.info()

df_title['Year'].describe().astype('int')

print("Unique Values :\n",df_title.nunique())

"""# 3. Analyze Data"""

no_of_rated_products_per_users = df.groupby(by='User_ID')['Rating'].count().sort_values(ascending=False)
no_of_rated_products_per_users.head()

no_of_rated_products_per_users.describe()

no_of_rated_products_per_movies = df.groupby(by='Movie_ID')['Rating'].count().sort_values(ascending=False)
no_of_rated_products_per_movies.head()

no_of_rated_products_per_movies.describe()

f = ['count','mean']
df_movie_summary = df.groupby('Movie_ID')['Rating'].agg(f)
df_movie_summary.index = df_movie_summary.index.map(int)
movie_benchmark = round(df_movie_summary['count'].quantile(0.7),0)
drop_movie_list = df_movie_summary[df_movie_summary['count'] < movie_benchmark].index

df__title = df_title.set_index('Movie_ID')

"""# 4. Recommendation Model

## 4.1 Collaborative Filtering - SVD
"""

model = SVD()

data = Dataset.load_from_df(df[['User_ID', 'Movie_ID', 'Rating']], Reader())

trainset, testset = train_test_split(data, test_size=0.3,random_state=10)

trainset = data.build_full_trainset()

model.fit(trainset)

predictions = model.test(testset)

accuracy.rmse(predictions)

def Recommendation(given_user_id,n_movies):
    given_user = df_title.copy()
    given_user = given_user.reset_index()
    given_user = given_user[~given_user['Movie_ID'].isin(drop_movie_list)]


    given_user['Estimated_Rating'] = given_user['Movie_ID'].apply(lambda x: model.predict(given_user_id, x).est)

    given_user = given_user.drop('Movie_ID', axis = 1)

    given_user = given_user.sort_values('Estimated_Rating', ascending=False)
    given_user.drop(['index'], axis = 1,inplace=True)
    given_user.reset_index(inplace=True,drop=True)
    return given_user.head(n_movies)

"""### Movie Recommendation for User - 712664"""

Recommendation(712664,10)

"""### Movie Recommendation for User - 2643029"""

Recommendation(2643029,5)

