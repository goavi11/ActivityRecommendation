import pandas as pd
import scipy.sparse as sp
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_data():
    movie_data = pd.read_csv('/Users/avishek/Documents/activityapp/Dataset/IMDb movies.csv', low_memory=False)
    rating_data = pd.read_csv('/Users/avishek/Documents/activityapp/Dataset/IMDb ratings.csv', low_memory=False)
    movie_data['original_title'] = movie_data['original_title'].str.lower()
    data = movie_data.join(rating_data["weighted_average_vote"])
    data = data.drop(columns=['imdb_title_id','title','date_published'])

    return(data)


# print(get_data()['genre'])

def combine_data(data):
    cols = ['genre', 'director']
    data['genre_director'] = data[cols].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
    return data


def transform_data(data_combine, data_plot):
    count = CountVectorizer(stop_words='english')
    count_matrix = count.fit_transform(data_combine['genre_director'])

    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data_plot['plot'])

    combine_sparse = sp.hstack([count_matrix, tfidf_matrix], format='csr')

    cosine_sim = cosine_similarity(combine_sparse, combine_sparse)

    return cosine_sim