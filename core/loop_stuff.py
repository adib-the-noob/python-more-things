books_list = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925}
]

for book in enumerate(books_list, start=1):
    print(f"Book {book[0]}: {book[1]['title']} by {book[1]['author']} ({book[1]['year']})")

print("--- Zip ---")
indexes = [20, 21, 22]
titles = ["The Catcher in the Rye", "Brave New World", "Fahrenheit 451"]
for book in zip(indexes, titles):
    print(f"Book ID {book[0]}: {book[1]}")