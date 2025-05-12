import streamlit as st
from recommender import train_model, get_recommendations

st.title("Рекомендатель книг")
model, df = train_model()

user_id = st.number_input("Введите ID пользователя", min_value=1, step=1)
if st.button("Показать рекомендации"):
    recommendations = get_recommendations(user_id, model, df)
    if recommendations:
        st.write("Рекомендованные книги:")
        for title in recommendations:
            st.markdown(f"- {title}")
    else:
        st.warning("Пользователь не найден или нет рекомендаций.")