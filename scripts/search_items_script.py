from app.services.item_reader import get_items_by_last_updated_dt

if __name__ == "__main__":
    input_data = {
        "dt_from": "2024-01-01 00:50:02",
        "dt_to": "2024-01-30 16:00:00"
    }
    result = get_items_by_last_updated_dt(input_data)
    print(result)