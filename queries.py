import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()
from django.db.models import Count,Q,Avg, Max, Min
from main.models import Author, Publisher, Book


# # Create publishers
# p1 = Publisher.objects.create(name="Penguin Books", founded=1935, location="London")
# p2 = Publisher.objects.create(name="HarperCollins", founded=1989, location="New York")

# # Create authors
# a1 = Author.objects.create(name="J.K. Rowling", birth_date="1965-07-31", nationality="British")
# a2 = Author.objects.create(name="George Orwell", birth_date="1903-06-25", nationality="British")

# # Create books
# b1 = Book.objects.create(
#     title="Harry Potter and the Philosopher's Stone",
#     genre="F",
#     publish_date="1997-06-26",
#     price=9.99,
#     publisher=p1
# )
# b1.authors.add(a1)

# b2 = Book.objects.create(
#     title="1984",
#     genre="F",
#     publish_date="1949-06-08",
#     price=7.99,
#     publisher=p2
# )
# b2.authors.add(a2)

# Get all books
# all_books = Book.objects.all()
# print(all_books)

# # Get a specific book
# book = Book.objects.get(title="1984")
# print(book)

# # Filter books
# fiction_books = Book.objects.filter(genre="F")
# print(fiction_books)
# expensive_books = Book.objects.filter(price__gt=10)
# print(expensive_books)

# #Get all books
# all_books = Book.objects.all()
# print("\nAll Books:")
# for book in all_books:
#     authors = ", ".join([author.name for author in book.authors.all()])
#     print(f" - {book.title} by {authors} | ${book.price}")

# Get a specific book
# try:
#     book = Book.objects.get(title="1984")
#     authors = ", ".join([author.name for author in book.authors.all()])
#     print(f"\nSpecific Book:\n - {book.title} by {authors} | ${book.price}")
# except Book.DoesNotExist:
#     print("\nBook '1984' not found.")

# # Filter books by genre
# fiction_books = Book.objects.filter(genre="F")
# print("\nFiction Books:")
# for book in fiction_books:
#     authors = ", ".join([author.name for author in book.authors.all()])
#     print(f" - {book.title} by {authors}")

# # Filter books with price > 10
# expensive_books = Book.objects.filter(price__gt=10)
# print("\nExpensive Books (Price > 10):")
# for book in expensive_books:
#     authors = ", ".join([author.name for author in book.authors.all()])
#     print(f" - {book.title} by {authors} | ${book.price}")

# #Update a book's price
# book = Book.objects.get(title="1984")
# book.price = 9.99
# book.save()

# #Bulk update
# Book.objects.filter(genre="F").update(price=3.99)

# # Delete a specific book
# Book.objects.get(title="1984").delete()

# # Delete all books by a publisher
# Book.objects.filter(publisher__name="Penguin Books").delete()

# books = Book.objects.all()
# for book in books:
#     print(book.title)

# penguin_books = Book.objects.filter(publisher__name='Penguin Books')
# for book in penguin_books:
#     print(book.title)

# publisher_stats = Publisher.objects.annotate(
#     book_count=Count('books'),
#     fiction_count=Count('books', filter=Q(books__genre='F'))
# )

# a1 = Author.objects.create(name="haha", birth_date="1965-07-31", nationality="British")
# Author.objects.filter(id=7).update(name="hehe")


# Author.objects.filter(id=7).delete()

# stats = Book.objects.aggregate(
#     avg_price=Avg('price'),
#     max_price=Max('price'),
#     min_price=Min('price')
# )

# print(stats)

# penguin_books = Book.objects.filter(publisher__name='Penguin Books')
# print(penguin_books.query)



# books = Book.objects.select_related('publisher').filter(publisher__name="Penguin Books")

# for book in books:
#     print(book.title)


# books = Book.objects.prefetch_related('authors').all()
# for book in books:
#     print(book.title)
#     print(book.publish_date)

# publishers = Publisher.objects.annotate(book_count=Count('books'))
# print(publishers.query)

publisher_stats = Publisher.objects.annotate(
    book_count=Count('books'),
    fiction_count=Count('books', filter=Q(books__genre='F'))
)
