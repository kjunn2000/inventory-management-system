from mysql.connector import Error
import item_creator

if __name__ == "__main__":
    request = {
        "name": "Notebook",
        "category": "Stationary",
        "price": "57222.222222225"
    }
    item_creator.create_or_update_item(request)