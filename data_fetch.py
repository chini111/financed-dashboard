import requests
import pandas as pd

API_URL='https://dummyjson.com/carts'

def fetch_transaction_data():
    response=requests.get(API_URL)
    data=response.json()
    transactions=[]
    for cart in data.get('carts', []):
        for item in cart.get('products', []):
            transactions.append({
                'title': item['title'],
                'price': item['price'],
                'quantity': item['quantity'],
                'total': item['total'],
                'discount': item['discountPercentage'],
            })
    return pd.DataFrame(transactions)
