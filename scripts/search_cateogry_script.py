from app.services.category_reader import aggregate_items_by_category

if __name__ == "__main__":
    input_category_data = {
        "category": "Home Use"
    }
    result = aggregate_items_by_category(input_category_data)

    print(result)
