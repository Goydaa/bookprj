import pandas as pd

def get_recommendations(df, liked_genres):
    return df[df["genre"].isin(liked_genres)]

def test_recommendations_by_genre():
    data = {
        "title": ["Book A", "Book B", "Book C", "Book D"],
        "genre": ["Fantasy", "Sci-Fi", "Fantasy", "Drama"]
    }
    df = pd.DataFrame(data)

    liked_genres = ["Fantasy"]
    recommended = get_recommendations(df, liked_genres)

    # Ожидается 2 книги с жанром Fantasy
    assert len(recommended) == 2
    assert all(g == "Fantasy" for g in recommended["genre"])
 
