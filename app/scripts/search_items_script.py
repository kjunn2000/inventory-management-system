from mysql.connector import Error
from services import item_reader

import json

if __name__ == "__main__":
    input_data = {
        "dt_from": "2024-01-01 00:50:02",
        "dt_to": "2024-01-30 10:00:00"
    }
    result = item_reader.get_items_by_last_updated_dt(input_data)

    json_result = json.dumps(result, indent=2)
    print(json_result)