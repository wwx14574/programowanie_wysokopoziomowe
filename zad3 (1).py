# Zajęcia 3 — Programowanie funkcyjne

class Book:
    def __init__(self, title, author, total_copies):
        self.__title = title
        self.__author = author
        self.__total_copies = total_copies
        self.__available_copies = total_copies
        self.__reservations = []

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def total_copies(self):
        return self.__total_copies

    @property
    def available_copies(self):
        return self.__available_copies

    @property
    def reservations(self):
        return self.__reservations

    def borrow_copy(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            return True
        return False

    def add_reservation(self, reader):
        self.__reservations.append(reader)

    def borrowed_count(self):
        return self.__total_copies - self.__available_copies

    def has_reservations(self):
        return len(self.__reservations) > 0

    def __str__(self):
        return f"{self.__title} - {self.__author} | dostępne: {self.__available_copies}/{self.__total_copies}"


class User:
    def __init__(self, login, password, role):
        self._login = login
        self._password = password
        self._role = role

    @property
    def login(self):
        return self._login

    @property
    def role(self):
        return self._role

    def authenticate(self, password):
        return self._password == password

    def menu(self):
        raise NotImplementedError("Klasa pochodna musi mieć własne menu.")


class Reader(User):
    def __init__(self, login, password):
        super().__init__(login, password, "czytelnik")
        self.__borrowed_books = []
        self.__extension_requests = []

    @property
    def borrowed_books(self):
        return self.__borrowed_books

    @property
    def extension_requests(self):
        return self.__extension_requests

    def add_borrowed_book(self, book):
        self.__borrowed_books.append(book)

    def add_extension_request(self, book):
        self.__extension_requests.append(book)

    def menu(self):
        print("\n=== MENU CZYTELNIKA ===")
        print("1. Przeglądaj katalog")
        print("2. Wypożycz książkę")
        print("3. Moje wypożyczenia")
        print("4. Prośba o przedłużenie")
        print("5. Wyszukaj / filtruj książki")
        print("6. Posortuj katalog")
        print("7. Zarezerwuj niedostępną książkę")
        print("8. Wyloguj")
        print("9. Zakończ program")


class Librarian(User):
    def __init__(self, login, password):
        super().__init__(login, password, "bibliotekarz")

    def menu(self):
        print("\n=== MENU BIBLIOTEKARZA ===")
        print("1. Przeglądaj katalog")
        print("2. Lista wypożyczeń")
        print("3. Obsługa próśb o przedłużenie")
        print("4. Wyszukaj / filtruj książki")
        print("5. Posortuj katalog")
        print("6. Statystyki")
        print("7. Wyloguj")
        print("8. Zakończ program")


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__extension_queue = []

    def add_book(self, book):
        self.__books.append(book)

    def add_user(self, user):
        self.__users.append(user)

    def find_user(self, login, password):
        for user in self.__users:
            if user.login == login and user.authenticate(password):
                return user
        return None

    def find_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                return book
        return None

    # Funkcja wyższego rzędu — przyjmuje funkcję jako argument
    def show_filtered_books(self, predicate):
        filtered_books = list(filter(predicate, self.__books))

        if not filtered_books:
            print("Brak książek spełniających warunek.")
            return

        for index, book in enumerate(filtered_books, start=1):
            print(f"{index}. {book}")

    def show_catalog(self):
        print("\n=== KATALOG KSIĄŻEK ===")
        self.show_filtered_books(lambda book: True)

    def search_books(self):
        print("\n=== WYSZUKIWANIE / FILTROWANIE ===")
        print("1. Szukaj po tytule lub autorze")
        print("2. Pokaż tylko dostępne książki")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            phrase = input("Podaj frazę: ").lower()

            # filter + lambda
            self.show_filtered_books(
                lambda book: phrase in book.title.lower() or phrase in book.author.lower()
            )

        elif choice == "2":
            # filter + lambda
            self.show_filtered_books(lambda book: book.available_copies > 0)

        else:
            print("Niepoprawny wybór.")

    def sort_books(self):
        print("\n=== SORTOWANIE KATALOGU ===")
        print("1. Według tytułu")
        print("2. Według autora")
        print("3. Według liczby dostępnych sztuk")

        choice = input("Wybierz opcję: ")

        if choice == "1":
            sorted_books = sorted(self.__books, key=lambda book: book.title.lower())
        elif choice == "2":
            sorted_books = sorted(self.__books, key=lambda book: book.author.lower())
        elif choice == "3":
            sorted_books = sorted(self.__books, key=lambda book: book.available_copies, reverse=True)
        else:
            print("Niepoprawny wybór.")
            return

        for index, book in enumerate(sorted_books, start=1):
            print(f"{index}. {book}")

    def borrow_book(self, reader):
        title = input("Podaj tytuł książki: ")
        book = self.find_book(title)

        if book is None:
            print("Nie znaleziono książki.")
            return

        if book.borrow_copy():
            reader.add_borrowed_book(book)
            print("Książka została wypożyczona.")
        else:
            print("Brak dostępnych egzemplarzy. Możesz zarezerwować tę książkę.")

    def reserve_book(self, reader):
        print("\n=== REZERWACJA KSIĄŻKI ===")
        title = input("Podaj tytuł książki do rezerwacji: ")
        book = self.find_book(title)

        if book is None:
            print("Nie znaleziono książki.")
            return

        if book.available_copies > 0:
            print("Ta książka jest dostępna, możesz ją wypożyczyć.")
            return

        if reader in book.reservations:
            print("Masz już rezerwację na tę książkę.")
            return

        book.add_reservation(reader)
        print("Książka została zarezerwowana.")

    def show_reader_borrowings(self, reader):
        print("\n=== MOJE WYPOŻYCZENIA ===")

        if not reader.borrowed_books:
            print("Brak wypożyczonych książek.")
            return

        for index, book in enumerate(reader.borrowed_books, start=1):
            print(f"{index}. {book.title} - {book.author}")

    def create_extension_request(self, reader):
        print("\n=== PROŚBA O PRZEDŁUŻENIE ===")

        if not reader.borrowed_books:
            print("Nie masz wypożyczonych książek.")
            return

        self.show_reader_borrowings(reader)
        title = input("Podaj tytuł książki do przedłużenia: ")

        for book in reader.borrowed_books:
            if book.title.lower() == title.lower():
                request = {
                    "reader": reader,
                    "book": book,
                    "status": "oczekuje"
                }

                self.__extension_queue.append(request)
                reader.add_extension_request(book)

                print("Prośba o przedłużenie została wysłana.")
                return

        print("Nie masz wypożyczonej książki o takim tytule.")

    def show_all_borrowings(self):
        print("\n=== WSZYSTKIE WYPOŻYCZENIA ===")

        borrowings = [
            (user.login, book)
            for user in self.__users
            if isinstance(user, Reader)
            for book in user.borrowed_books
        ]

        if not borrowings:
            print("Brak aktualnych wypożyczeń.")
            return

        for login, book in borrowings:
            print(f"Użytkownik: {login} | Książka: {book.title} - {book.author}")

    def handle_extension_requests(self):
        print("\n=== OBSŁUGA PRÓŚB O PRZEDŁUŻENIE ===")

        pending_requests = [
            request for request in self.__extension_queue
            if request["status"] == "oczekuje"
        ]

        if not pending_requests:
            print("Brak próśb do obsłużenia.")
            return

        for index, request in enumerate(pending_requests, start=1):
            reader = request["reader"]
            book = request["book"]

            reservation_info = (
                "TAK" if book.has_reservations() else "NIE"
            )

            print(
                f"{index}. {reader.login} prosi o przedłużenie: {book.title} "
                f"| Rezerwacja na tę książkę: {reservation_info}"
            )

        choice = input("Podaj numer prośby do obsłużenia: ")

        if not choice.isdigit():
            print("Niepoprawny wybór.")
            return

        request_index = int(choice) - 1

        if request_index < 0 or request_index >= len(pending_requests):
            print("Nie ma takiej prośby.")
            return

        decision = input("Akceptujesz prośbę? (t/n): ")

        if decision.lower() == "t":
            pending_requests[request_index]["status"] = "zaakceptowana"
            print("Prośba została zaakceptowana.")
        elif decision.lower() == "n":
            pending_requests[request_index]["status"] = "odrzucona"
            print("Prośba została odrzucona.")
        else:
            print("Niepoprawna decyzja.")

    def show_statistics(self):
        print("\n=== STATYSTYKI BIBLIOTEKARZA ===")

        # comprehension
        borrowed_counts = [book.borrowed_count() for book in self.__books]

        total_borrowings = sum(borrowed_counts)

        # filter + lambda
        borrowed_books = list(filter(lambda book: book.borrowed_count() > 0, self.__books))

        if borrowed_books:
            most_popular = max(borrowed_books, key=lambda book: book.borrowed_count())
            print(f"Najpopularniejsza książka: {most_popular.title}")
        else:
            print("Najpopularniejsza książka: brak danych")

        print(f"Liczba aktywnych wypożyczeń ogółem: {total_borrowings}")

        readers = list(filter(lambda user: isinstance(user, Reader), self.__users))

        sorted_readers = sorted(
            readers,
            key=lambda reader: len(reader.borrowed_books),
            reverse=True
        )

        # comprehension
        reader_stats = {
            reader.login: len(reader.borrowed_books)
            for reader in sorted_readers
        }

        print("Czytelnicy według liczby wypożyczonych książek:")

        if not reader_stats:
            print("Brak czytelników.")
            return

        for login, count in reader_stats.items():
            print(f"{login}: {count}")


def login_user(library):
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        print("\n=== LOGOWANIE ===")
        login = input("Login: ")
        password = input("Hasło: ")

        user = library.find_user(login, password)

        if user is not None:
            print(f"Zalogowano jako: {user.login} ({user.role})")
            return user

        attempts += 1
        print(f"Błędny login lub hasło. Pozostało prób: {max_attempts - attempts}")

    print("Przekroczono limit prób logowania.")
    return None


def handle_reader_choice(library, reader, choice):
    if choice == "1":
        library.show_catalog()
    elif choice == "2":
        library.borrow_book(reader)
    elif choice == "3":
        library.show_reader_borrowings(reader)
    elif choice == "4":
        library.create_extension_request(reader)
    elif choice == "5":
        library.search_books()
    elif choice == "6":
        library.sort_books()
    elif choice == "7":
        library.reserve_book(reader)
    elif choice == "8":
        print("Wylogowano.")
        return "logout"
    elif choice == "9":
        return "exit"
    else:
        print("Niepoprawny wybór.")

    return "continue"


def handle_librarian_choice(library, choice):
    if choice == "1":
        library.show_catalog()
    elif choice == "2":
        library.show_all_borrowings()
    elif choice == "3":
        library.handle_extension_requests()
    elif choice == "4":
        library.search_books()
    elif choice == "5":
        library.sort_books()
    elif choice == "6":
        library.show_statistics()
    elif choice == "7":
        print("Wylogowano.")
        return "logout"
    elif choice == "8":
        return "exit"
    else:
        print("Niepoprawny wybór.")

    return "continue"


def user_session(library, user):
    while True:
        user.menu()
        choice = input("Wybierz opcję: ")

        if isinstance(user, Reader):
            result = handle_reader_choice(library, user, choice)
        elif isinstance(user, Librarian):
            result = handle_librarian_choice(library, choice)
        else:
            result = "logout"

        if result == "logout":
            return "logout"

        if result == "exit":
            return "exit"


def create_library():
    library = Library()

    library.add_book(Book("Wiedźmin", "Andrzej Sapkowski", 3))
    library.add_book(Book("Lalka", "Bolesław Prus", 2))
    library.add_book(Book("Pan Tadeusz", "Adam Mickiewicz", 4))
    library.add_book(Book("Zbrodnia i kara", "Fiodor Dostojewski", 1))
    library.add_book(Book("Harry Potter", "J.K. Rowling", 5))

    library.add_user(Reader("ania", "1234"))
    library.add_user(Reader("jan", "abcd"))
    library.add_user(Reader("ola", "qwerty"))
    library.add_user(Librarian("admin", "admin"))

    return library


def run_program():
    library = create_library()

    while True:
        user = login_user(library)

        if user is None:
            print("Program zakończony.")
            break

        result = user_session(library, user)

        if result == "exit":
            print("Program zakończony.")
            break


run_program()