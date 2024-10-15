from main import przetworz_wejscie

def test_przetworz_wejscie_standard_input():
    wejscie = "   ,,,WITAJ, SWIECIE!!! To jest przykladowy TEKST, ktory bedzie OBRABIANy,,,   "
    expected_lista = ['witaj', 'swiecie!!!', 'to', 'jest', 'przykladowy', 'tekst', 'ktory', 'bedzie', 'obrabiany']
    expected_liczba = 9
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_z_pustymi_elementami():
    wejscie = ",,, , alfa,, beta,,gamma,"
    expected_lista = ['alfa', 'beta', 'gamma']
    expected_liczba = 3
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_z_malymi_literami():
    wejscie = "   Python, PYTHON , python"
    expected_lista = ['python', 'python', 'python']
    expected_liczba = 3
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba

def test_przetworz_wejscie_puste():
    wejscie = "   ,, ,,,   "
    expected_lista = []
    expected_liczba = 0
    wynik_lista, wynik_liczba = przetworz_wejscie(wejscie)
    assert wynik_lista == expected_lista
    assert wynik_liczba == expected_liczba
