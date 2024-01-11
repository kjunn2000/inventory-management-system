import sys
import os

parent_dir = os.path.dirname(os.path.realpath(__file__))
print(parent_dir)
# Add the parent directory to sys.path
sys.path.append(parent_dir)

from mysql.connector import Error
from services import item_creator
import json

if __name__ == "__main__":
    request = {
        "name": "TV",
        "category": "Home Use",
        "price": "3.222222225"
    }
    result = item_creator.create_or_update_item(request)
    json_result = json.dumps(result, indent=2)
    print(json_result)
