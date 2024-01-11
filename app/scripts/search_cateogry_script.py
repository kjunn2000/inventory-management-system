from mysql.connector import Error
from services import category_reader

import json

if __name__ == "__main__":
    input_category_data = {
        "category": "all"
    }
    result = category_reader.aggregate_items_by_category(input_category_data)

    json_result = json.dumps(result, indent=2)
    print(json_result)
