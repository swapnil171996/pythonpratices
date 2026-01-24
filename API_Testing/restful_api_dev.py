'''
API  Types:
--> SOUP API
--> Request API
protocol:http
HTTP Methods:

->GET
->POST
->PUT
->PATCH
->DELETE

API Response Code:

100-199 : Information status
200-299 : Success status
300-399 : Re-directional status
400-499 : Client Error Code
500-599:Server Error Code





'''

import requests
def execute_get_method():
    url = "https://api.restful-api.dev/objects"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    print(response.status_code)#200
    data=response.json()
    for val in data:
        print(val)
#execute_get_method()


#[{"id":"1","name":"Google Pixel 6 Pro","data":{"color":"Cloudy White","capacity":"128 GB"}},{"id":"2","name":"Apple iPhone 12 Mini, 256GB, Blue","data":null},{"id":"3","name":"Apple iPhone 12 Pro Max","data":{"color":"Cloudy White","capacity GB":512}},{"id":"4","name":"Apple iPhone 11, 64GB","data":{"price":389.99,"color":"Purple"}},{"id":"5","name":"Samsung Galaxy Z Fold2","data":{"price":689.99,"color":"Brown"}},{"id":"6","name":"Apple AirPods","data":{"generation":"3rd","price":120}},{"id":"7","name":"Apple MacBook Pro 16","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}},{"id":"8","name":"Apple Watch Series 8","data":{"Strap Colour":"Elderberry","Case Size":"41mm"}},{"id":"9","name":"Beats Studio3 Wireless","data":{"Color":"Red","Description":"High-performance wireless noise cancelling headphones"}},{"id":"10","name":"Apple iPad Mini 5th Gen","data":{"Capacity":"64 GB","Screen size":7.9}},{"id":"11","name":"Apple iPad Mini 5th Gen","data":{"Capacity":"254 GB","Screen size":7.9}},{"id":"12","name":"Apple iPad Air","data":{"Generation":"4th","Price":"419.99","Capacity":"64 GB"}},{"id":"13","name":"Apple iPad Air","data":{"Generation":"4th","Price":"519.99","Capacity":"256 GB"}}]

def get_specific_ids():
    url = ("https://api.restful-api.dev/objects?id=3&id=5&id=10")
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

#get_specific_ids()
#[{"id":"3","name":"Apple iPhone 12 Pro Max","data":{"color":"Cloudy White","capacity GB":512}},{"id":"5","name":"Samsung Galaxy Z Fold2","data":{"price":689.99,"color":"Brown"}},{"id":"10","name":"Apple iPad Mini 5th Gen","data":{"Capacity":"64 GB","Screen size":7.9}}]

def get_one_single_ids():
    url = ("https://api.restful-api.dev/objects/7")
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

#get_one_single_ids()
#{"id":"7","name":"Apple MacBook Pro 16","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}}
import json
def create_new_entry():
    url = "https://api.restful-api.dev/objects"
    payload = json.dumps({
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
#create_new_entry()
#{"id":"ff8081819782e69e019b5545ff0c73fc","name":"Apple MacBook Pro 16","createdAt":"2025-12-25T11:30:09.292+00:00","data":{"year":2019,"price":1849.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB"}}

def update_entry(id):
    url = f"https://api.restful-api.dev/objects/{id}"
    payload = json.dumps({
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 2049.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "color": "silver"
   }
}
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
#update_entry("ff8081819782e69e019b5896aaf2796a")
#{"id":"ff8081819782e69e019b5896aaf2796a","name":"Apple MacBook Pro 16","updatedAt":"2025-12-26T02:59:04.146+00:00","data":{"year":2019,"price":2049.99,"CPU model":"Intel Core i9","Hard disk size":"1 TB","color":"silver"}}

def partically_update(id):
    url=f"https://api.restful-api.dev/objects/{id}"
    payload = json.dumps(
        {
   "name": "Apple MacBook Pro 160 (Updated Name)"}
    )
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)
#partically_update("ff8081819782e69e019b5896aaf2796a")
#{"id":"ff8081819782e69e019b5896aaf2796a","name":"Apple MacBook Pro 160 (Updated Name)","updatedAt":"2025-12-26T03:07:29.504+00:00","data":null}


def delete_mobile_device(id):
    url=f"https://api.restful-api.dev/objects/{id}"
    payload = {}

    headers = {}

    response = requests.request("DELETE", url, headers=headers, data=payload)

    print(response.text)
    print(response.status_code)
delete_mobile_device("ff8081819782e69e019b5896aaf2796a")
#{"message":"Object with id = ff8081819782e69e019b5896aaf2796a has been deleted."}
#200
