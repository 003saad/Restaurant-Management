class Menu:
    def __init__(self):
        self.menu_items = []

    def add_menu_item(self, item):
        self.menu_items.append(item)

    def find_item(self, item_name):
        for item in self.menu_items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.menu_items.remove(item)
            print(f"Item '{item_name}' removed from the menu.")
        else:
            print(f"Item '{item_name}' not found in the menu.")

    def show_menu(self):
        print("******* Menu ******")
        print("Name\tPrice\tQuantity")
        for item in self.menu_items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

