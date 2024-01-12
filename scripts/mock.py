from unittest.mock import Mock


def getMockItemJson():
    return {
        "name": "TV1111",
        "category": "Home Use",
        "price": "663333.222222225"
    }


def getMockItem():
    return Mock(name="TV1111", category="Home Use", price="663333.222222225")
