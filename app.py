import streamlit as st
import pandas as pd
import os

#  переименовываем русские названия столбцов, если такие есть 
if os.path.exists("books.csv"):
    try:
        temp_df = pd.read_csv("books.csv", encoding="utf-8")
        temp_df.rename(columns={
            "Название": "title",
            "Автор": "author",
            "Жанр": "genre",
            "Описание": "description"
        }, inplace=True)
        temp_df.to_csv("books.csv", index=False, encoding="utf-8")
    except Exception as e:
        st.warning(f"Ошибка при попытке конвертировать заголовки: {e}")

#  Загрузка книг 
@st.cache_data
def load_books():
    try:
        df = pd.read_csv("books.csv", encoding="utf-8")
        if df.empty:
            st.error("Файл 'books.csv' пуст.")
        return df
    except pd.errors.EmptyDataError:
        st.error("Файл 'books.csv' пуст или поврежден.")
        return pd.DataFrame()
    except FileNotFoundError:
        st.error("Файл 'books.csv' не найден.")
        return pd.DataFrame()

books_df = load_books()

#  Инициализация сессии 
if "likes" not in st.session_state:
    st.session_state.likes = {}  
if "read_later" not in st.session_state:
    st.session_state.read_later = set()

# Фильтрация 
st.sidebar.title("🔍 Фильтрация")
view_option = st.sidebar.radio(
    "Выбери режим просмотра:",
    ("Все книги", "👍 Понравившиеся", "👎 Не понравившиеся",  "📜 Читать позже")
)

display_df = pd.DataFrame()

if view_option == "Все книги":
    display_df = books_df.copy()
elif view_option == "👍 Понравившиеся":
    liked_ids = [i for i, v in st.session_state.likes.items() if v == "like"]
    display_df = books_df.loc[books_df.index.isin(liked_ids)]
elif view_option == "👎 Не понравившиеся":
    disliked_ids = [i for i, v in st.session_state.likes.items() if v == "dislike"]
    display_df = books_df.loc[books_df.index.isin(disliked_ids)]
elif view_option == "📜 Читать позже":
    display_df = books_df.loc[books_df.index.isin(st.session_state.read_later)]

#  Заголовок 
st.title(" Каталог книг")

# Отображение книг
if display_df.empty:
    st.info("Нет книг для отображения в этом разделе.")
else:
    for idx, row in display_df.iterrows():
        st.subheader(row.get("title", "Без названия"))
        st.text(f"Автор: {row.get('author', 'Не указан')}")
        st.text(f"Жанр: {row.get('genre', 'Не указан')}")

        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("👍 Нравится", key=f"like_{idx}"):
                st.session_state.likes[idx] = "like"
        with col2:
            if st.button("👎 Не нравится", key=f"dislike_{idx}"):
                st.session_state.likes[idx] = "dislike"
        with col3:
            if idx in st.session_state.read_later:
                if st.button("❌ Убрать", key=f"remove_later_{idx}"):
                    st.session_state.read_later.remove(idx)
            else:
                if st.button("📜 Читать позже", key=f"read_later_{idx}"):
                    st.session_state.read_later.add(idx)

st.divider()

#  Рекомендации 
liked_books = [row for i, row in books_df.iterrows() if st.session_state.likes.get(i) == "like"]
if liked_books:
    st.header("Рекомендации по твоим вкусам")
    liked_df = pd.DataFrame(liked_books)
    genres = liked_df["genre"].dropna().unique()

    rec_df = books_df[books_df["genre"].isin(genres)]
    rec_df = rec_df[~rec_df.index.isin(st.session_state.likes.keys())]

    for idx, row in rec_df.head(10).iterrows():
        st.subheader(row.get("title", "Без названия"))
        st.text(f"Автор: {row.get('author', 'Не указан')}")
        st.text(f"Жанр: {row.get('genre', 'Не указан')}")

