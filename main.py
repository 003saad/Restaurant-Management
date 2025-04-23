from food_item import FoodItem
from menu import Menu
from restaurant import Restaurant
from users import Customer,Admin, Employee
from orders import Order

mamar_restaurant = Restaurant("Mamar Restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    customer = Customer(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'\nWelcome {customer.name} to the Restaurant Management System')
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. PayBill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")


def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    admin = Admin(name=name, email=email, phone=phone, address=address)

    while True:
        print(f'\nWelcome {admin.name} to the Restaurant Management System')
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employees")
        print("4. View Items")
        print("5.Delete Item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mamar_restaurant, item)

        elif choice == 2:
            name = input("Enter employee name: ")
            phone = input("Enter employee phone: ")
            email = input("Enter employee email: ")
            address = input("Enter employee address: ")
            designation = input("Enter employee designation: ")
            age = input("Enter employee age: ")
            salary = input("Enter employee salary: ")
            employee = Employee(name, email, phone, address, age, designation, salary)
            admin.add_employee(mamar_restaurant, employee)
        elif choice == 3:
            admin.view_employee(mamar_restaurant)
        elif choice == 4:
            admin.view_menu(mamar_restaurant)
        elif choice == 5:
            item_name = input("Enter item name to delete: ")
            admin.remove_item(mamar_restaurant, item_name)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")


while True:
    print("Welcome to the Restaurant Management System")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")
