# Function to display the current stock
def display_stock(stock):
    print("Current Stock:")
    for book, quantity in stock.items():
        print(f"{book}: {quantity}")

# Function to update the stock of a book
def update_stock(stock, book, quantity):
    if book in stock:
        stock[book] += quantity
        print(f"Stock of '{book}' updated to {stock[book]}")
    else:
        print("Book not found in stock.")

# Function to add a new book to the stock
def add_book(stock, book, quantity):
    if book in stock:
        print("Book already exists in stock. Use 'update' to change the quantity.")
    else:
        stock[book] = quantity
        print(f"New book '{book}' added with stock {quantity}")

# Function to delete a book from the stock
def delete_book(stock, book):
    if book in stock:
        del stock[book]
        print(f"Book '{book}' deleted from stock.")
    else:
        print("Book not found in stock.")

stock={}

while True:
    print("\nMenu:")
    print("1. Display Stock")
    print("2. Update Stock")
    print("3. Add Book")
    print("4. Delete Book")
    print("5. Exit")
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        display_stock(stock)
    elif choice == '2':
        book = input("Enter the book title: ")
        quantity = int(input("Enter the quantity to update (positive for addition, negative for subtraction): "))
        update_stock(stock, book, quantity)
    elif choice == '3':
        book = input("Enter the new book title: ")
        quantity = int(input("Enter the initial stock quantity: "))
        add_book(stock, book, quantity)
    elif choice == '4':
        book = input("Enter the book title to delete: ")
        delete_book(stock, book)
    elif choice == '5':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
