import pytest
from main import przetworz_wejscie

def test_przetworz_wejscie_standard_input():
    wejscie = "   ,,,WITAJ, ŚWIECIE!!! To jest przykładowy TEKST, który będzie OBRABIANy,,,   "
    expected_lista = ['witaj', 'świecie!!! to jest przykładowy tekst', 'który będzie obrabiany']
    expected_liczba = 3
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_empty_input():
    wejscie = ""
    expected_lista = []
    expected_liczba = 0
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_multiple_commas():
    wejscie = ",,, hej, alfa,beat, aaa"
    expected_lista = ['hej', 'alfa', 'beat', 'aaa']
    expected_liczba = 4
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_extra_spaces():
    wejscie = "   Python   ,    jest    ,   super   "
    expected_lista = ['python', 'jest', 'super']
    expected_liczba = 3
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba
