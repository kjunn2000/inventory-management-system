from app.services.item_creator import create_or_update_item

if __name__ == "__main__":
    request = {
        "name": "short",
        "category": "cloth",
        "price": "16.22"
    }
    result = create_or_update_item(request)
    print(result)
