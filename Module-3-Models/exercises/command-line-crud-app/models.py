class Item:
    def __init__(self, identifier, name, description):
        self.identifier = identifier
        self.name = name
        self.description = description


class ItemManager:
    def __init__(self):
        self.items = []

    def create_item(self, identifier, name, description):
        item = Item(identifier, name, description)
        self.items.append(item)
        return item

    def view_all_items(self):
        return self.items

    def search_items(self, filter_func):
        return [item for item in self.items if filter_func(item)]

    def view_single_item(self, identifier):
        item = next(
            (item for item in self.items if item.identifier == identifier), None
        )
        return item

    def update_item(self, identifier, new_name, new_description):
        item = self.view_single_item(identifier)
        if item:
            item.name = new_name
            item.description = new_description
        return item

    def delete_item(self, identifier):
        self.items = [item for item in self.items if item.identifier != identifier]
