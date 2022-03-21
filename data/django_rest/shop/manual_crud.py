import requests

r = requests.post(url='http://127.0.0.1:8000/api/v1/products/',
                  data={
                        "title": "iPad Air 3",
                        "weight": 599.99,
                        "price": 600,
                        "is_stock": False,
                        "valid_until": "2022-12-10",
                        "brand_id": 3
                  })

print(r.status_code)