import requests

def get_categories():
    url = 'http://ec2-34-236-250-113.compute-1.amazonaws.com:9000/categories/'
    r = requests.get(url)
    categories = r.json()
    category_choices = [(c['id'], c['name']) for c in categories]
    return category_choices