import pytest
from functions import *



def test_string_input_validation(monkeypatch):
    #Test happy cases using expected vs actual and assert 

    #simulating a  valid input
    monkeypatch.setattr('builtins.input', lambda _: 'John')
    expected = "John"
    actual = string_input_validation("What is your name?")
    assert expected == actual 

        #simulating a valid input but with a space
    monkeypatch.setattr('builtins.input', lambda _: 'John Obi')
    expected = "John Obi"
    actual = string_input_validation("What is your name?")
    assert expected == actual 




def test_string_input_unhappy(monkeypatch):
    #simulating an invalid input with special characters, then a valid input
    inputs = iter(['John-Obi','John!','J0hn', '', 'John'])  #start with invalid input
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))  #processes list of inputs individually
    #this avoids the test looping for every by simulating that a user would have finally enter a valid input
    expected = "John"
    
    actual = string_input_validation("What is your name?")
    
    assert expected == actual


def test_integer_input_validation_happy(monkeypatch):

    monkeypatch.setattr('builtins.input', lambda _: '42')

    expected = 42

    actual = integer_input_validation("Enter a number:")

    assert expected == actual


def test_integer_input_validation_unhappy(monkeypatch):

    inputs = iter(['abc', '-5', '0', '10'])  

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    expected = 10

    actual = integer_input_validation("Enter a number:")

    assert expected == actual

def test_confirmation_yes(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '1')
    expected = None  # `confirmation` breaks the loop but returns nothing if user chooses 'Yes'
    actual = confirmation("Do you confirm?")
    assert actual == expected


def test_confirmation_no(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    expected = 2
    actual = confirmation("Do you confirm?")
    assert expected == actual


def test_confirmation_unhappy(monkeypatch):
    inputs = iter(['0', '3', '2'])  
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    expected = 2
    actual = confirmation("Do you confirm?")
    assert expected == actual
