import unittest

from app.models.new_item_dto import NewItemDto


class TestNewItemDto(unittest.TestCase):

    def test_new_item_dto_instantiation(self):
        new_item_dto = NewItemDto(name='TV', category='Electronics', price=499.99)

        self.assertEqual(new_item_dto.name, 'TV')
        self.assertEqual(new_item_dto.category, 'Electronics')
        self.assertEqual(new_item_dto.price, 499.99)

    def test_new_item_dto_repr_method(self):
        new_item_dto = NewItemDto(name='TV', category='Electronics', price=499.99)
        
        expected_repr = "Item(name=TV, category=Electronics, price=499.99)"
        self.assertEqual(repr(new_item_dto), expected_repr)