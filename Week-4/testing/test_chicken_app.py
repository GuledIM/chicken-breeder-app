import pytest
from unittest.mock import MagicMock
from src.app import *

def test_chicken_class():
    # Create a chicken for the test
    c = Chicken("Lucy", "Leghorn", 12)
    
    # Check that attributes are set correctly
    assert c.name == "Lucy"
    assert c.breed == "Leghorn"
    assert c.age == 12

def test_print_all_chickens(monkeypatch):
    # Create a fake cursor to mock database interactions
    fake_cursor = MagicMock()
    fake_cursor.fetchall.return_value = [(1, "Lucy", "Leghorn", 12)]

    # Handling the cursor and clr_terminal INSIDE src.app
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)

    # Create instance of the class
    manager = ChickenManager()

    # Run the method
    manager.print_all_chickens()

    # Assertions to confirm behaviour
    fake_cursor.execute.assert_called_once_with("SELECT * FROM chickens")
    fake_cursor.fetchall.assert_called_once()

def test_print_all_chickens_db_error(monkeypatch):
    fake_cursor = MagicMock()
    fake_cursor.execute.side_effect = Exception("Database Error")

    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)

    manager = ChickenManager()

    with pytest.raises(Exception, match="Database Error"):
        manager.print_all_chickens()


def test_add_chicken_happy(monkeypatch):
    fake_cursor = MagicMock()
    fake_conn = MagicMock()

    # Patch the database and helper functions
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.conn", fake_conn)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)
    monkeypatch.setattr("src.app.confirmation", lambda x: 1)  # user confirms yes
    monkeypatch.setattr("src.app.string_input_validation", lambda x: "Lucy")
    monkeypatch.setattr("src.app.integer_input_validation", lambda x: 12)
    monkeypatch.setattr(time, "sleep", lambda x: None)

    manager = ChickenManager()
    manager.add_chicken()

    # Ensure the DB methods were called
    fake_cursor.execute.assert_called_once()
    fake_conn.commit.assert_called_once()

def test_add_chicken_user_cancels(monkeypatch):
    fake_cursor = MagicMock()

    # Patch what the class actually uses
    monkeypatch.setattr("src.app.confirmation", lambda x: 2)  # user cancels
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)
    monkeypatch.setattr(time, "sleep", lambda x: None)  # skip waiting

    manager = ChickenManager()
    manager.add_chicken()

    # Since user canceled, cursor.execute will NOT be called
    fake_cursor.execute.assert_not_called()

def test_update_chicken_happy(monkeypatch):
    fake_cursor = MagicMock()

    # Patch globals that update_chicken uses
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.confirmation", lambda x: 1)  # user confirms update
    monkeypatch.setattr("src.app.user_ID_selection_validation", lambda a, b: 1)  # select ID=1
    monkeypatch.setattr("src.app.string_input_validation", lambda x: "LucyNew")  # new name
    monkeypatch.setattr("src.app.integer_input_validation", lambda x: 14)       # new age
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)  # skip clearing
    monkeypatch.setattr(time, "sleep", lambda x: None)          # skip delay
    monkeypatch.setattr("src.app.ChickenManager.print_all_chickens", lambda self: None)  # skip printing

    manager = ChickenManager()
    manager.update_chicken()

    # Check that cursor.execute was called to update the DB
    fake_cursor.execute.assert_called_once_with(
        "UPDATE chickens SET name = %s, breed = %s, age = %s WHERE id = %s",
        ("LucyNew", "LucyNew", 14, 1)
    )

def test_delete_chicken_happy(monkeypatch):
    fake_cursor = MagicMock()
    fake_conn = MagicMock()

    # Patch what ChickenManager actually uses
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.conn", fake_conn)
    monkeypatch.setattr("src.app.confirmation", lambda x: 1)  # user confirms deletion
    monkeypatch.setattr("src.app.user_ID_selection_validation", lambda a, b: 1)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)
    monkeypatch.setattr("src.app.ChickenManager.print_all_chickens", lambda self: None)
    monkeypatch.setattr(time, "sleep", lambda x: None)  # skip actual sleep

    manager = ChickenManager()
    manager.delete_chicken()

    # Check that the deletion and commit happened
    fake_cursor.execute.assert_called_once()
    fake_conn.commit.assert_called_once()

def test_delete_chicken_user_cancels(monkeypatch):
    fake_cursor = MagicMock()

    monkeypatch.setattr("src.app.confirmation", lambda x: 2)
    monkeypatch.setattr("src.app.cursor", fake_cursor)
    monkeypatch.setattr("src.app.clr_terminal", lambda: None)

    manager = ChickenManager()
    manager.delete_chicken()

    fake_cursor.execute.assert_not_called()

