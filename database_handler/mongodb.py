from pymongo import MongoClient

def get_womens_clothing_data():
    """
    This function returns a list of measurements from the database that have been modified.
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client['tenet-clothes-data']
    collection = db['clothes-data']

    query = {"category": "Women's Clothing"}
    result = collection.find(query)

    data = []
    for item in result:
        data.append({
            'title': item['title'],
            'description': item['description'],
            'price': item['price'],
            'size': item['size']
        })

    return data
