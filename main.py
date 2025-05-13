import os
from book_class.book_management import Book
from menu_functions.search_books import search_book
from menu_functions.compare_books import compare_books
from menu_functions.show_all_books import show_all_books

book_1 = Book("1984", "Джордж Орвелл", 1949, 328, "Антиутопія")
book_2 = Book("Машина часу", "Герберт Веллс", 1895, 118, "Наукова фантастика")
book_3 = Book("Прощавай, зброє", "Ернест Хемінгуей", 1929, 355, "Роман")
book_4 = Book("Сяйво", "Стівен Кінг", 1977, 447, "Жахи")
book_5 = Book("Інститут", "Стівен Кінг", 2019, 560, "Трилер")

book_list = [book_1, book_2, book_3, book_4, book_5]

def print_menu():
    while True:
        os.system('cls')

        print("МЕНЮ:")
        print("1. Показати всі книги")
        print("2. Пошук книги за назвою")
        print("3. Порівняти книги за кількістю сторінок")
        print("4. Вийти")
        
        choice = input("Виберіть опцію: ")
        if choice == "1":
            show_all_books(book_list)
        elif choice == "2":
            search_book(book_list)
        elif choice == "3":
            compare_books(book_list)
        elif choice == "4":
            exit()
        else:
            print("Невірний вибір. Спробуйте ще раз.\n")

print_menu()