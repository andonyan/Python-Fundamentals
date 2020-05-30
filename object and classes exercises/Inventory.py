class Inventory:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.actual_capacity = capacity
        self.items = []

    def __repr__(self):
        return f'Items: {", ".join(self.items)}.\nCapacity left: {self.actual_capacity}'

    def add_item(self, item):
        if self.actual_capacity > 0:
            self.items.append(item)
            self.actual_capacity -= 1
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return self.__capacity


inventory = Inventory(2.7)
print(inventory)
