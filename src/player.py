# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room, items=[]):  # constructor
        self.current_room = current_room
        self.items = items

    def return_items(self):
        return self.items

    def print_items(self):
        for i in self.items:
            print(f'Item: {i.name} Descrption: {i.description}')

    def add_item(self, item):
        return self.items.append(item)

    def remove_item(self, item):
        return self.items.remove(item)
