# Customer
# Employee
#  Admin

from abc import ABC
from orders import Order

class User(ABC):
    def __init__(self, name, email,phone,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, phone,email,address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_menu()

    def add_to_cart(self,restaurant,item_name,quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Not enough quantity available.")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item Added!!!")
        else:
            print("Item not found in the menu.")

    def view_cart(self):
        print("*****View Cart*****")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price:  {self.cart.total_price}")

    def pay_bill(self):
        print(f'Total Price: {self.cart.total_price} paid successfully')
        self.cart.clear()

class Employee(User):
    def __init__(self, name, email,phone, address, age,designation,salary):
        super().__init__(name, phone,email,address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self,name,email,phone,address):
        super().__init__(name,phone,email,address)
        # self.employess = []

    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)

    def view_employee(self,restaurant):
        restaurant.view_employee()

    def add_new_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)

    def remove_item(self,restaurant,item):
        restaurant.menu.remove_item(item)

    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
        








# # ad = Admin("Karim","123123","karim@gmail.com","Dhaka")
# # ad.add_employee("Sagor","asasasad@","1234567890","Dhaka",25,"waiter",20000)

# mamar_rastaurant = Restaurant("Mamar Restaurant")
# mn = Menu()
# item = FoodItem("Pizza", 500, 10)
# item2 = FoodItem("Burger",10,30)
# admin = Admin("Rahim","rahim124@gmail.com",123123,"Dhaka")
# admin.add_new_item(mamar_rastaurant,item)
# admin.add_new_item(mamar_rastaurant,item2)
# # mn.add_menu_item(item)
# # mn.add_menu_item(item2)
# # mn.show_menu()


# # ad.view_employee()
# # mamar_rastaurant = Restaurant("Mamar Restaurant")
# customer1 = Customer("Rahim","rahim124@gmail.com",123123,"Dhaka")
# customer1.view_menu(mamar_rastaurant)

# item_name = input("Enter the item name to add to cart: ")
# quantity = int(input("Enter the quantity: "))
# customer1.add_to_cart(mamar_rastaurant,item_name,quantity)
# customer1.view_cart()