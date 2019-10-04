# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    def __str__(self):
        toprint = f'room: {self.name}, description: {self.description}\n'
        for item in self.items:
            toprint += f'Items: {item} - {item.description}'
            return toprint