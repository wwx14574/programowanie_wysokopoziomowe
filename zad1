# Lista książek dostępnych w bibliotece
ksiazki = [
    {"tytul": "Wiedzmin", "autor": "Andrzej Sapkowski", "sztuki": 3},
    {"tytul": "Lalka", "autor": "Boleslaw Prus", "sztuki": 2},
    {"tytul": "Pan Tadeusz", "autor": "Adam Mickiewicz", "sztuki": 4},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "sztuki": 1},
    {"tytul": "Harry Potter", "autor": "J.K. Rowling", "sztuki": 5}
]


# Lista użytkowników
uzytkownicy = [
    {"login": "ania", "haslo": "1234", "rola": "czytelnik", "wypozyczenia": []},
    {"login": "jan", "haslo": "abcd", "rola": "czytelnik", "wypozyczenia": []},
    {"login": "ola", "haslo": "qwerty", "rola": "czytelnik", "wypozyczenia": []}
]


def znajdz_uzytkownika(login, haslo):
    for uzytkownik in uzytkownicy:
        if uzytkownik["login"] == login and uzytkownik["haslo"] == haslo:
            return uzytkownik
    return None

# Logowanie

def logowanie():
    liczba_prob = 0

    while liczba_prob < 3:
        print("------------------------------------------------------------")
        print("\n++++ LOGOWANIE ++++")
        login = input("Podaj login: ")
        haslo = input("Podaj haslo: ")

        uzytkownik = znajdz_uzytkownika(login, haslo)

        if uzytkownik is not None:
            print(f"\nZalogowano pomyslnie. Witaj, {uzytkownik['login']}!")
            return uzytkownik
        else:
            liczba_prob += 1
            print(f"Bledny login lub haslo. Pozostalo prob: {3 - liczba_prob}")

    print("\nPrzekroczono limit prob logowania.")
    return None

# Wyświetlanie menu

def wyswietl_menu():
    print("------------------------------------------------------------")
    print("\n++++ MENU GLOWNE ++++")
    print("1. Przegladaj katalog")
    print("2. Wypozycz ksiazke")
    print("3. Moje wypozyczenia")
    print("4. Wyloguj")
    print("5. Zakoncz program")

# Funkcje systemu

def przegladaj_katalog():
    print("------------------------------------------------------------")
    print("\n++++ KATALOG KSIAZEK ++++")
    for numer, ksiazka in enumerate(ksiazki, start=1):
        print(
            f"{numer}. Tytul: {ksiazka['tytul']}, "
            f"Autor: {ksiazka['autor']}, "
            f"Dostepne sztuki: {ksiazka['sztuki']}"
        )


def znajdz_ksiazke_po_tytule(tytul):
    for ksiazka in ksiazki:
        if ksiazka["tytul"].lower() == tytul.lower():
            return ksiazka
    return None


def wypozycz_ksiazke(zalogowany_uzytkownik):
    print("------------------------------------------------------------")
    print("\n=== WYPOZYCZANIE KSIAZKI ===")
    tytul = input("Podaj tytul ksiazki do wypozyczenia: ")

    ksiazka = znajdz_ksiazke_po_tytule(tytul)

    if ksiazka is None:
        print("Nie znaleziono ksiazki o podanym tytule.")
        return

    if ksiazka["sztuki"] > 0:
        ksiazka["sztuki"] -= 1
        zalogowany_uzytkownik["wypozyczenia"].append(ksiazka["tytul"])
        print(f'Ksiazka "{ksiazka["tytul"]}" zostala wypozyczona.')
    else:
        print("Brak dostepnych sztuk tej ksiazki.")


def moje_wypozyczenia(zalogowany_uzytkownik):
    print("\n=== MOJE WYPOZYCZENIA ===")

    if len(zalogowany_uzytkownik["wypozyczenia"]) == 0:
        print("Nie masz aktualnie wypozyczonych zadnych ksiazek.")
    else:
        for numer, tytul in enumerate(zalogowany_uzytkownik["wypozyczenia"], start=1):
            print(f"{numer}. {tytul}")

# Menu użytkownika

def menu_uzytkownika(zalogowany_uzytkownik):
    while True:
        wyswietl_menu()
        wybor = input("\nWybierz opcje: ")

        if wybor == "1":
            przegladaj_katalog()
        elif wybor == "2":
            wypozycz_ksiazke(zalogowany_uzytkownik)
        elif wybor == "3":
            moje_wypozyczenia(zalogowany_uzytkownik)
        elif wybor == "4":
            print("Wylogowano z systemu.")
            return "wyloguj"
        elif wybor == "5":
            print("Program zostaje zakonczony.")
            return "koniec"
        else:
            print("Niepoprawny wybor. Sprobuj ponownie.")

# Główna funkcja programu

def uruchom_program():
    while True:
        zalogowany_uzytkownik = logowanie()

        if zalogowany_uzytkownik is None:
            print("Program zostaje zakonczony.")
            break

        wynik = menu_uzytkownika(zalogowany_uzytkownik)

        if wynik == "koniec":
            break

# Start programu

uruchom_program()
