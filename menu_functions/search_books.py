import os
from book_class.book_management import Book

def search_book(book_list):
    os.system('cls')

    search_title = input("Введіть назву книги яку Ви шукаєте: ")
    found_book = Book.find_book_by_title(search_title, book_list)

    if found_book:
        print(f"Книга '{search_title}' знайдена:\n")
        print(found_book.get_info())
    else:
        print(f"Книга з назвою '{search_title}' не знайдена.")

    input("Натисніть `Enter`, щоб повернутись до меню...")