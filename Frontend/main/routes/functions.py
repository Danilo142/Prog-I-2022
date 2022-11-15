from flask import request, current_app, redirect, url_for

import requests, json

def get_poems_by_id(id, page = 1, per_page = 10):
    api_url = f'{current_app.config['API_URL']}/poems' 

    data = {"id": id, "page": page, "per_page": per_page, "user_id": id}

    headers = get_headers(without_token = True)

    return requests.get(api_url, data = data, headers = headers)


def get__poem(id):
    api_url = f'{current_app.config['API_URL']}/poems/{id}'

    headers = get_headers()

    return requests.get(api_url, headers = headers)

def get_poems(page = 1, per_page = 3):
    api_url = f'{current_app.config['API_URL']}/poems'

    data = {"page": page, "per_page": per_page}

    headers = get_headers(without_token = True)

    return requests.get(api_url, data = data, headers = headers)

def delete_poem(id):
    api_url = f'{current_app.config['API_URL']}/poems/{id}'

    headers = get_headers()

    return requests.delete(api_url, headers = headers)


def get_user_info(id):
    api_url = f'{current_app.config['API_URL']}/users/{id}'

    headers = get_headers()

    return requests.get(api_url, headers = headers)

def get_user(id):
    api_url = f'{current_app.config['API_URL']}/users/{id}'

    headers = get_headers()

    return requests.get(api_url, headers = headers)

def get_username(user_id):
    api_url = f'{current_app.config['API_URL']}/users/{user_id}'

    headers = get_headers()

    user = json.loads(response.text)
    return user['username']


def get_qualifications_by_poem_id(id):
    api_url = f'{current_app.config['API_URL']}/qualifications'

    data = {"poem_id": id}

    headers = get_headers(without_token = True)

    return requests.get(api_url, data = data, headers = headers)


def json_loads(response):
    return json.loads(response.text)


def get_headers(without_token = False):
    if without_token:
        return {'Content-Type': 'application/json', 'Accept': f'Bearer{jwt}'}
    else:
        return {'Content-Type': 'application/json'}
    
def get_token():
    return request.cookies.get('token')


def get_jwt():
    return request.cookies.get('jwt')

def get_user_id():
    return request.cookies.get('user_id')

def redirect_to(url):
    return redirect(url_for(url))