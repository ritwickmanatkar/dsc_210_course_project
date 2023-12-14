import numpy as np
import pandas as pd
from neuralrecommender.glocalk import GlocalK
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


CSV_FILE_PATH = '/Users/ritwickmanatkar/Downloads/BookReviews.csv'

def read_data():
    return pd.read_csv(CSV_FILE_PATH)


def print_relevant_info(df):
    print(f"Shape: {df.shape}")
    print(f"Info: \n{df.info()}")


def get_encoder(df):
    encoder = LabelEncoder()
    encoder.fit(df['user_id'])
    return encoder


def encode_user_id_column(df, encoder):
    encoded_ids = encoder.transform(df['user_id'])
    df['encoded_user_ids'] = encoded_ids
    return df[['encoded_user_ids', 'book_id', 'rating']]


def glocalk_implementation(df):
    ratings_matrix = df.pivot(
        index='encoded_user_ids',
        values='rating',
        columns=['book_id']
    ).fillna(0)

    n_u = ratings_matrix.shape[0]  # num of users
    n_m = ratings_matrix.shape[1]

    train_r, test_r = train_test_split(ratings_matrix.to_numpy(), test_size=20, random_state=45)

    train_m = np.greater(train_r, 1e-12).astype('float32')
    test_m = np.greater(test_r, 1e-12).astype('float32')

    recommender = GlocalK()
    metrics = recommender.fit(train_r)
    print(metrics)

    res = recommender.predict(np.arange(n_u - 1))

    k = 50
    ground_truth = np.argsort(-test_r, axis=0)[:k, :].T.tolist()
    recommended = np.argsort(-res, axis=0)[:k, :].T.tolist()
    random = np.random.randint(0, n_m, (n_u, k)).T.tolist()

    print(f"Baseline (random): {np.sqrt(mean_squared_error(ground_truth, random))}")
    print(f"GLocalK: {np.sqrt(mean_squared_error(ground_truth, recommended))}")


if __name__ == '__main__':
    df = read_data()
    print_relevant_info(df)
    encoder = get_encoder(df)
    new_df = encode_user_id_column(df, encoder)

    glocalk_implementation(new_df)