import requests


def http_response():
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response.json()


def response_headers():
    url = 'https://httpbin.org/response-headers?freeform=Response%20via%20API'
    response = requests.get(url)
    return response.json()


def post_http():
    url = 'https://httpbin.org/post'
    data = 'posted via API'
    response = requests.post(url, json=data)
    return response.json()


def patch_http():
    url = 'https://httpbin.org/patch'
    data = 'posted via API'
    response = requests.patch(url, json=data)
    return response.json(), response.status_code


def post_todo():
    url = 'https://jsonplaceholder.typicode.com/users/1/todos'
    data = {
        'user_id': 1,
        'task': 'buy butter',
        'completed': False
    }
    response = requests.post(url, json=data)
    return response.json()


def put_todo():
    url = 'https://jsonplaceholder.typicode.com/users/1/todos'
    data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": True
    }
    response = requests.put(url, json=data)
    return response.json(), response.status_code
