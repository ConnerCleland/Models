import unittest
from models import ItemManager
from helpers import Item


class TestCRUDOperations(unittest.TestCase):
    def setUp(self):
        self.item_manager = ItemManager()

    def test_create_item(self):
        item = self.item_manager.create_item(1, "Item1", "Description1")
        self.assertEqual(item.identifier, 1)
        self.assertEqual(item.name, "Item1")
        self.assertEqual(item.description, "Description1")

    def test_view_all_items(self):
        self.item_manager.create_item(1, "Item1", "Description1")
        items_list = self.item_manager.view_all_items()
        self.assertEqual(len(items_list), 1)

    def test_search_items(self):
        self.item_manager.create_item(1, "Item1", "Description1")
        self.item_manager.create_item(2, "Item2", "Description2")
        self.item_manager.create_item(3, "Item3", "Description3")
        filtered_items = self.item_manager.search_items(
            lambda x: x.name.startswith("Item")
        )
        self.assertEqual(len(filtered_items), 3)

    def test_view_single_item(self):
        self.item_manager.create_item(1, "Item1", "Description1")
        item = self.item_manager.view_single_item(1)
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Item1")

    def test_update_item(self):
        self.item_manager.create_item(1, "Item1", "Description1")
        updated_item = self.item_manager.update_item(1, "NewItem", "NewDescription")
        self.assertIsNotNone(updated_item)
        self.assertEqual(updated_item.name, "NewItem")
        self.assertEqual(updated_item.description, "NewDescription")

    def test_delete_item(self):
        self.item_manager.create_item(1, "Item1", "Description1")
        self.item_manager.delete_item(1)
        self.assertEqual(len(self.item_manager.view_all_items()), 0)


if __name__ == "__main__":
    unittest.main()
