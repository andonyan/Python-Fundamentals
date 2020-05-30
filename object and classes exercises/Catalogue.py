class Catalogue:

    def __init__(self, n):
        self.name = n
        self.products = []

    def __repr__(self):
        output_string = f'Items in the {self.name} catalogue:'
        self.products.sort()
        for item in self.products:
            output_string += f'\n{item}'
        return output_string

    def add_product(self, product):
        self.products.append(product)

    def get_by_letter(self, first_letter):
        return [item for item in self.products if item[0] == first_letter]


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
