import unittest
from datetime import datetime

from app.models.item import Item


class TestItem(unittest.TestCase):

    def test_item_instantiation(self):
        item = Item(id=1, name='Laptop', category='Electronics', price=999.99, last_updated_dt=datetime(2022, 1, 1, 12, 0))

        self.assertEqual(item.id, 1)
        self.assertEqual(item.name, 'Laptop')
        self.assertEqual(item.category, 'Electronics')
        self.assertEqual(item.price, 999.99)
        self.assertEqual(item.last_updated_dt, datetime(2022, 1, 1, 12, 0))

    def test_item_repr_method(self):
        item = Item(id=1, name='Laptop', category='Electronics', price=999.99, last_updated_dt=datetime(2022, 1, 1, 12, 0))

        expected_repr = "Item(id=1, name=Laptop, category=Electronics, price=999.99, last_updated_dt=2022-01-01 12:00:00)"
        self.assertEqual(repr(item), expected_repr)

    def test_item_to_json_method(self):
        item = Item(id=1, name='Laptop', category='Electronics', price=999.99, last_updated_dt=datetime(2022, 1, 1, 12, 0))

        expected_json = {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99}
        self.assertEqual(item.to_json(), expected_json)
