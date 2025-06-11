import pytest

class SessionStateMock:
    def __init__(self):
        self.likes = {}

def test_like_dislike_toggle():
    session = SessionStateMock()

    # Пользователь лайкает книгу с id = 1
    session.likes[1] = "like"
    assert session.likes[1] == "like"

    # Пользователь меняет лайк на дизлайк
    session.likes[1] = "dislike"
    assert session.likes[1] == "dislike"

    # Удаление оценки
    del session.likes[1]
    assert 1 not in session.likes
 
