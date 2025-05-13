import os
from book_class.book_management import Book

def compare_books(book_list):
    os.system('cls')

    print("Список доступних для порівння книг:")
    for book in book_list:
        print(f" -> {book.title}")

    title_1 = input("\nВведіть назву першої книги для порівняння: ")
    title_2 = input("Введіть назву другої книги для порівняння: ")

    book_1 = Book.find_book_by_title(title_1, book_list)
    book_2 = Book.find_book_by_title(title_2, book_list)

    if not book_1 or not book_2:
        print("Одна або обидві книги не знайдено.")
    else:
        result = Book.compare_pages(book_1, book_2)
        if result == 1:
            print(f"\n'{book_1.title}' має більше сторінок, ніж '{book_2.title}'.")
        elif result == -1:
            print(f"\n'{book_1.title}' має менше сторінок, ніж '{book_2.title}'.")
        else:
            print(f"\n'{book_1.title}' та '{book_2.title}' мають однакову кількість сторінок.")

    input("\nНатисніть `Enter`, щоб повернутись до меню...")