def przetworz_wejscie(wejscie):
    pass

def main():
    wejscie = input("Podaj kilka slow oddzielonych przecinkami: ")
    lista_slow, liczba_slow = przetworz_wejscie(wejscie)
    print("Lista slow:", lista_slow, "#", liczba_slow)

if __name__ == "__main__":
    main()
