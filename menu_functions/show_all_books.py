import os

def show_all_books(book_list):
    os.system('cls')

    for book in book_list:
        print("=======================================")
        print(book.get_info())
        print("---------------------------------------")
        print(f"Сучасна книга? <- {book.is_modern()}")
        print(f"Жанр книги Наукова фантастика? <- {book.is_genre('Наукова фантастика')}")

    print("=======================================")

    input("Натисніть `Enter`, щоб повернутись до меню...")