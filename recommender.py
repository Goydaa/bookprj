import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

def train_model():
    df = pd.read_csv("ratings.csv")
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df[['user_id', 'book_id', 'rating']], reader)
    trainset, _ = train_test_split(data, test_size=0.25)
    model = SVD()
    model.fit(trainset)
    return model, df

def get_recommendations(user_id, model, df):
    books = pd.read_csv("books.csv")
    rated_books = df[df.user_id == user_id]["book_id"].tolist()
    unrated_books = books[~books["book_id"].isin(rated_books)]
    predictions = [(book["title"], model.predict(user_id, book["book_id"]).est)
                   for _, book in unrated_books.iterrows()]
    recommendations = sorted(predictions, key=lambda x: x[1], reverse=True)[:5]
    return [title for title, _ in recommendations]