def przetworz_wejscie(wejscie):
    wejscie = wejscie.strip().replace(",,", ",")
    lista_slow = wejscie.split(",")
    lista_slow = [slowo.strip().lower() for slowo in lista_slow if slowo.strip()]
    return lista_slow, len(lista_slow)


def main():
    wejscie = input("Podaj kilka slow oddzielonych przecinkami: ")
    lista_slow, liczba_slow = przetworz_wejscie(wejscie)
    print("Lista slow:", lista_slow, "#", liczba_slow)

if __name__ == "__main__":
    main()
