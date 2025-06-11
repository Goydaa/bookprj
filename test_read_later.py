 
import pytest

class SessionStateMock:
    def __init__(self):
        self.read_later = set()

def test_add_to_read_later():
    session = SessionStateMock()

    session.read_later.add(5)
    assert 5 in session.read_later

def test_remove_from_read_later():
    session = SessionStateMock()
    session.read_later.add(3)
    session.read_later.remove(3)
    assert 3 not in session.read_later
