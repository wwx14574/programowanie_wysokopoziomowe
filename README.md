# Biblioteka

Aplikacja zaliczeniowa z przedmiotu Programowanie Wysokopoziomowe.

---

## Zajęcia 1 - Programowanie strukturalne

Aplikacja biblioteczna napisana z wykorzystaniem programowania strukturalnego.

### Funkcjonalności

- logowanie użytkownika
- limit 3 prób logowania
- przeglądanie katalogu książek
- wypożyczanie książek
- podgląd własnych wypożyczeń
- wylogowanie

### Dane

Program działa na danych zapisanych na sztywno w kodzie:

- co najmniej 5 książek
- 3 użytkowników z rolą „czytelnik”

### Uruchomienie
bash
python3 zad1.py

---

## Zajęcia 2 - Programowanie obiektowe

Refaktoryzacja aplikacji do wersji obiektowej (OOP).

### Zastosowane klasy

- Book
- User
- Reader
- Librarian
- Library

### Funkcjonalności

#### Czytelnik

- logowanie użytkownika
- przeglądanie katalogu książek
- wypożyczanie książek
- podgląd własnych wypożyczeń
- wysyłanie próśb o przedłużenie
- wylogowanie

#### Bibliotekarz

- przeglądanie katalogu książek
- podgląd wszystkich wypożyczeń
- obsługa próśb o przedłużenie
- wylogowanie

### Programowanie obiektowe

W projekcie zastosowano:

- klasy i obiekty
- dziedziczenie
- hermetyzację
- polimorfizm
- metodę specjalną __str__

### Uruchomienie

bash
python3 zad2.py
