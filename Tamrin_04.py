class Book:
    def __init__(s, book_title, book_author, book_price):
        s.book_title = book_title
        s.book_author = book_author
        s.book_price = book_price
    
    def details_display(s):
        print(f"Title: {s.book_title}")
        print(f"Author: {s.book_author}")
        print(f"Price: {s.book_price}")
        print("-" * 20)
    
    def discount_apply(s, discount_percent):
        discount_amount = s.book_price * (discount_percent / 100)
        s.book_price = s.book_price - discount_amount

print("Enter number of books: ")
num_books = int(input())

books = []

for i in range(num_books):
    print(f"\nEnter book {i+1} info:")
    title = input("Title: ")
    author = input("Author: ")
    price = float(input("Price: "))
    
    book = Book(title, author, price)
    books.append(book)

print("\nBefore discount:")
for book in books:
    book.details_display()

print("\nApply discount:")
for i, book in enumerate(books):
    discount = float(input(f"Enter discount percent for book {i+1} ({book.book_title}): "))
    book.discount_apply(discount)

print("\nAfter discount:")
for book in books:
    book.details_display()