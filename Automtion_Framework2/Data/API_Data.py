import requests
import json

api_url="https://api.restful-api.dev/objects"

create_entry_payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
print(create_entry_payload)
API_headers = {
        'Content-Type': 'application/json'
    }

print("create_entry_payload")
