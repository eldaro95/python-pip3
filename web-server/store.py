import requests

def get_cat():
    r =requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text)) #para ver que es un string aunque tenga formato de lista
    cat=r.json()
    for category in cat:
        print(category['name'])