from mysql.connector import Error
import item_creator
import item_reader
import json

# if __name__ == "__main__":
#     request = {
#         "name": "Notebook",
#         "category": "Stationary",
#         "price": "57222.222222225"
#     }
#     result = item_creator.create_or_update_item(request)
#     json_result = json.dumps(result, indent=2)
#     print(json_result)


if __name__ == "__main__":
    input_data = {
        "dt_from": "2024-01-14 00:50:02",
        "dt_to": "2024-01-30 10:00:00"
    }
    result = item_reader.get_items_by_last_updated_dt(input_data)

    json_result = json.dumps(result, indent=2)
    print(json_result)