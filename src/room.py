# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=None):  # constructor
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def return_items(self):
        return self.items

    def print_items(self):
        for i in self.items:
            print(f'Item: {i.name} Descrption: {i.description}')

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item):
        return self.items.remove(item)
