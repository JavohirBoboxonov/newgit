class Book:
    def __init__(self, name, autor, price, about, book_id):
        self.name = name 
        self.autor = autor
        self.price = price
        self.about = about
        self.book_id = book_id

    def update_book(self):
        print("1 Book name \n 2 Book price \n 3 Autor \n 4 about \n 5 break")
        while True:
            choice = input("Enter Your Choice")
            
            if choice == "1":
                self.name = choice
            elif choice == "2":
                self.price = choice
            elif choice == "3":
                self.autor = choice
            elif choice == "4":
                self.about = choice
            else:
                print("Dastur tugadi")
                break            
    def get_info(self):
        return f"""
Name: {self.name}
Autor: {self.autor}
Price: {self.price}
About: {self.about}
Book ID: {self.book_id}
"""

class Group:
    def __init__(self, name, group_id):
        self.name = name
        self.group_id = group_id
        self.books = []

    def add_books(self):
        name = input("Enter Book Name")
        autor = input("Enter Book`s Autor")
        try:
            price = int(input("Enter Price: "))
            book_id = int(input("Enter book id"))
        except ValueError:
            print("error info must be intager")
            return
        about = input("What about book")
        book = Book(name, autor, price, about, book_id)
        self.books.append(book)
    
    def remove_book(self):
        book_id = int(input("Enter Book id"))
        for i in self.books:
            if book_id in self.books:
                self.books.remove(book_id)
                print("kitob o`chirildi")
            else:
                print("Kitob topilmadi")

    def view_group(self):
        return f"""
Name:{self.name}
ID:{self.group_id}
"""
    
class Library:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def add_group(self):
        name = input("Enter Group name")
        try:
            group_id = int(input("Enter Group id: "))
        except ValueError:
            print("Group ID must be integer")
            return
        group = Group(name, group_id)
        self.groups.append(group)


    def view_Library(self):
        return f"Library Name: {self.name}"

    def show_groups(self):
        if not self.groups:
            print("No groups avaible")
            return
        for g in self.groups:
            print(g.view_group())
    
    def select_group(self):
        if not self.groups:
            print("No groups available.")
            return None

        try:
            gid = int(input("Enter Group ID to select: "))
        except ValueError:
            print("ID must be integer")
            return None

        for g in self.groups:
            if g.group_id == gid:
                return g

        print("Group not found")
        return None
    
def menu():
    print("""
==========================
       LIBRARY MENU
==========================
1. Add Group
2. View All Groups
3. Add Book to Group
4. Find Book in Group
5. View Library Info
6. Exit
==========================
""")


library = Library("My Library")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        library.add_group()

    elif choice == "2":
        library.show_groups()

    elif choice == "3":
        group = library.select_group()
        if group:
            group.add_books()

    elif choice == "4":
        group = library.select_group()
        if group:
            group.get_one()

    elif choice == "5":
        print(library.view_Library())

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice, try again.")