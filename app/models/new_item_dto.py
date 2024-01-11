class NewItemDto:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def __repr__(self):
        return f"Item(name={self.name}, category={self.category}, price={self.price})"
