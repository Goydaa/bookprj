import pandas as pd
import pytest
from app import load_books

# Проверка: файл загружается и не пустой
def test_load_books_not_empty():
    df = load_books()
    assert not df.empty, "Файл пуст или не загружен"

# Проверка: у книги есть необходимые колонки
def test_books_columns():
    df = load_books()
    required = {"title", "author", "genre"}
    assert required.issubset(df.columns), "Отсутствуют обязательные столбцы"

# Проверка: уникальность названий книг
def test_unique_titles():
    df = load_books()
    assert df["title"].is_unique, "Названия книг не уникальны"
