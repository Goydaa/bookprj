import pandas as pd

def filter_books(df, likes, mode):
    if mode == "like":
        return df[df.index.isin([i for i, v in likes.items() if v == "like"])]
    elif mode == "dislike":
        return df[df.index.isin([i for i, v in likes.items() if v == "dislike"])]
    return df

def test_filter_liked_books():
    df = pd.DataFrame({
        "title": ["Book A", "Book B", "Book C"],
        "author": ["Author A", "Author B", "Author C"]
    })

    likes = {0: "like", 1: "dislike"}

    liked = filter_books(df, likes, "like")
    assert len(liked) == 1
    assert liked.iloc[0]["title"] == "Book A"

    disliked = filter_books(df, likes, "dislike")
    assert len(disliked) == 1
    assert disliked.iloc[0]["title"] == "Book B"
 
