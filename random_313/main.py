class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' от {self.author}({self.year})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку!\n")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Книга '{book.title}' была удалена!!\n")
                return
        print(f"Книга '{book.title}' не найдена!!!\n")

    def find_book_by_title(self, title):
        found_books = [book for book in self.books if title.lower() in book.title.lower()]
        if found_books:
            print("Найденные книги: ")
            for book in found_books:
                print(book)
            print()
        else:
            print(f"Книга c названием '{title}' не найдена!!!!\n")

    def find_book_by_author(self, author):
        found_books = [book for book in self.books if author.lower() in book.author.lower()]
        if found_books :
            print("Найденные книги: ")
            for book in found_books:
                print(book)
            print()
        else :
            print(f"Книг '{author}' не найдено!!!!\n")

    def show_all_books(self):
        if self.books:
            print("Найденные книги: ")
            for book in self.books:
                print(book)
            print()
        else:
            print("В библиотеки книжек нет!!!!!\n")


def match_making(library):
    choice = input('Выберите номер действия: ')

    match choice:
        case '1':
            title = input("Name of book: ")
            author = input("Author name: ")
            year = input('Year of book: ')
            book = Book(title, author, year)
            library.add_book(book)

        case '2':
            title = input('Name of book: ')
            library.remove_book(title)

        case '3':
            title = input('Name of book: ')
            library.find_book_by_title(title)

        case '4':
            author = input('Name of author: ')
            library.find_book_by_author(author)

        case '5':
            library.show_all_books()

        case '6':
            print("Exit...")
            return False

        case _:
            print("Untrack sign... Try again.\n")
    return True


def menu():
    library = Library()

    while True:
        print('Выберите действие:\n'
              '1. Добавьте книгу.\n'
              '2. Удалить книгу.\n'
              '3. Найти книгу по названию.\n'
              '4. Найти книгу по автору.\n'
              '5. Вывести все книги.\n'
              '6. Выйти.\n')

        if not match_making(library):
            break


if __name__ == "__main__":
    menu()



