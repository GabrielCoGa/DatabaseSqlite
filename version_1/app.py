#https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p

from Filedatabase import *

USER_CHOICE = """
Enter:
- 'a' to add a new book
_ 'l' to list all books
_ 'r' to mark a book as read
_ 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknow commad. Please try again.")

        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    add_book(name, author)


def list_books():
    books_return = get_all_books()

    for book_return in books_return:
        read = 'YES' if book_return['read'] else 'NO'# if 1 = YES else 0 NO
        print("author {} with title {} read {}".format(book_return['author'], book_return['name'], read))

def prompt_read_book():
    name = input('Enter the name of de book you just finished reading: ')
    
    mark_book_as_read(name)


def prompt_delete_book():
    name = input('Enter the name of the book you wish to delete: ')

    delete_book(name)


#iniciamos la app
menu()
