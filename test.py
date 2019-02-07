import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resources(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
def create_resource():
    new_emp={
    'eno':2000,
    'ename':'Katrina',
    'esal':20000,
    'eaddr':'Mumbai',
    }
    r=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
    print(r.status_code)
    # print(r.text)
    print(r.json())
def update_resource(id):
    new_data={
    'id':id,
    'eno':7777,
    'ename':'Kareena',
    'eaddr':'Lanka',
    'esal':15000
    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
def delete_resource(id):
    data={
    # 'id':id,
    }
    r=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
delete_resource(14)
