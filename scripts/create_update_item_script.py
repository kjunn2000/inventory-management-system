from app.services.item_creator import create_or_update_item

if __name__ == "__main__":
    request = {
        "name": "TV111",
        "category": "Home Use",
        "price": "663.222222225"
    }
    result = create_or_update_item(request)
    print(result)
