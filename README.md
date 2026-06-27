###Biblioteka - Zajęcia 3

Aplikacja zaliczeniowa z przedmiotu Programowanie Wysokopoziomowe.

---

Temat

Biblioteka - rozszerzenie projektu z wykorzystaniem programowania funkcyjnego.

---

Funkcjonalności

Funkcje dostępne dla czytelnika

- logowanie użytkownika,
- limit 3 prób logowania,
- przeglądanie katalogu książek,
- wypożyczanie książek,
- podgląd własnych wypożyczeń,
- wysyłanie próśb o przedłużenie wypożyczenia,
- wyszukiwanie książek po tytule lub autorze,
- filtrowanie dostępnych książek,
- sortowanie katalogu,
- rezerwacja niedostępnych książek,
- wylogowanie.

Funkcje dostępne dla bibliotekarza

- przeglądanie katalogu,
- podgląd wszystkich wypożyczeń,
- obsługa próśb o przedłużenie,
- wyszukiwanie i filtrowanie książek,
- sortowanie katalogu,
- wyświetlanie statystyk biblioteki,
- wylogowanie.

---

Zastosowane elementy programowania funkcyjnego

W projekcie wykorzystano:

- "lambda",
- "filter()",
- "sorted()" z parametrem "key",
- list comprehensions,
- dict comprehensions,
- funkcję wyższego rzędu przyjmującą funkcję jako argument.

---

Dane początkowe

Program uruchamia się z przykładowymi danymi:

Książki

- Wiedźmin
- Lalka
- Pan Tadeusz
- Zbrodnia i kara
- Harry Potter

Użytkownicy

Login| Hasło| Rola
ania| 1234| czytelnik
jan| abcd| czytelnik
ola| qwerty| czytelnik
admin| admin| bibliotekarz

---

Uruchomienie

python zad3.py

lub

python3 zad3.py
