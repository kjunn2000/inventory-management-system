class Item:
    def __init__(self, id, name, category, price, last_updated_dt):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.last_updated_dt = last_updated_dt

    def __repr__(self):
        return f"Item(id={self.id}, name={self.name}, category={self.category}, price={self.price}, last_updated_dt={self.last_updated_dt})"

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "price": self.price
        }
