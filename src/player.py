# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []
    def __str__(self):
        toprint = f'name: {self.name}, room: {self.current_room}, Inventory: '
        for item in self.items:
            toprint += f'{item}'
            return toprint

    name = str
    current_room = str