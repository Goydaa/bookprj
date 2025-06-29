# **КАТАЛОГ КНИГ**

---

## **ОПИСАНИЕ ПРОЕКТА**

Веб-приложение **Каталог книг** предназначено для удобного просмотра, фильтрации и взаимодействия с коллекцией книг через браузер. Проект позволяет отмечать понравившиеся и непонравившиеся книги, добавлять их в список «Читать позже» и получать персональные рекомендации на основе предпочтений пользователя.

---

## **ФУНКЦИОНАЛ ПРОЕКТА**

- **Просмотр списка всех книг**
- **Фильтрация по категориям:**
  - Все книги
  - Понравившиеся книги
  - Непонравившиеся книги
  - Список «Читать позже**
- **Возможность ставить отметки:**
  - Нравится
  - Не нравится
  - Читать позже
- **Система рекомендаций** по жанрам, учитывающая интересы пользователя
- **Работа с CSV-файлом**, содержащим данные о книгах

---

## **ИСПОЛЬЗУЕМЫЕ ТЕХНОЛОГИИ**

- **Python** — язык программирования
- **Streamlit** — библиотека для создания веб-интерфейсов
- **Pandas** — библиотека для работы с таблицами и данными
- **CSV** — формат хранения базы книг

---

## **ПРЕИМУЩЕСТВА ПРОЕКТА**

- Простота запуска и настройки
- Удобный, понятный интерфейс
- Быстрая работа с большим количеством книг
- Сохранение пользовате


---

## **ТРЕБОВАНИЯ ДЛЯ ЗАПУСКА**

- Python **3.10** или выше
- Установленные библиотеки из `requirements.txt`

---

## **ИНСТРУКЦИЯ ПО ЗАПУСКУ**

1. Установите все зависимости:
   
pip install -r requirements.txt

2. Откройте CMD и впишите:

cd (путь, где находится файл)

venv\Scripts\activate

streamlit run app.py


---

## **АЛГОРИТМ РАБОТЫ ПРИЛОЖЕНИЯ**

1. Загрузка данных из файла `books.csv`
2. Отображение каталога книг
3. Пользователь может:
   - Поставить отметку "Нравится"
   - Поставить отметку "Не нравится"
   - Добавить в "Читать позже"
4. Генерация рекомендаций по жанрам
5. Изменения сохраняются в сессии




