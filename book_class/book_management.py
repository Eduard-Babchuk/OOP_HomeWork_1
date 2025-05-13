class Book:
    def __init__(self, title, author, year, pages, genre):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.genre = genre
    
    def get_info(self):
        return f"Назва: {self.title}; \nАвтор: {self.author}; \nРік видання: {self.year}; \nСторінок: {self.pages}."

    def is_modern(self):
        return self.year > 2010
    
    def is_genre(self, genre):
        return self.genre.lower() == genre.lower()
    
    @staticmethod
    def find_book_by_title(title, book_list):
        for book in book_list:
            if book.title.lower() == title.lower():
                return book
        return None
    
    @staticmethod
    def compare_pages(book1, book2):
        if book1.pages > book2.pages:
            return 1 
        elif book1.pages < book2.pages:
            return -1  
        else:
            return 0