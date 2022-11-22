
from flask import Flask, Blueprint, render_template, current_app, make_response, request, redirect, url_for
import requests, json




app = Blueprint('app', __name__, url_prefix='/')

@app.route('/')
def index():
    api_url = f'{current_app.config["API_URL"]}/poems'
    data = {"page": 1, "per_page": 10}
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, data = data, headers = headers)
    print(response.status_code)
    print(response.text)
    poems = json.loads(response.text)
    print (poems)
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email, password)

        if email != None and password != None:
            api_url = f'{current_app.config["API_URL"]}/users/login'
            data = {"email": email, "password": password}
            headers = {"Content-Type": "application/json"}
            response = requests.post(api_url, data = data, headers = headers)
            print(response.status_code)
            print(response.text)
            if response.status_code == 200:
                user = json.loads(response.text)
                print(user)
                response = make_response(redirect(url_for('app.index')))
                response.set_cookie('token', user['token'])
                return response
            else:
                return render_template('login.html', error = 'Invalid email or password')
        
        else:
            return render_template('login.html')
       


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/home')
def user_main():
    if request.cookies.get('access_token'):
         api_url = f'{current_app.config["API_URL"]}/users'
         headers = {"Content-Type": "application/json"}
         response = requests.get(api_url, headers = headers)
         print(response.status_code)
         print(response.text)
         poems = json.loads(response.text)
         print (poems)
         return render_template('user_main.html', poems = poems["poems"])
    else:
            return redirect(url_for('app.login'))

@app.route('/profile')
def user_profile():
    if request.cookies.get('access_token'):
        api_url = f'{current_app.config["API_URL"]}/users'
        headers = {"Content-Type": "application/json"}
        data = {"page": 1, "per_page": 10}
        response = requests.get(api_url, data = data, headers = headers)
        return render_template('user_profile.html', poemsf = ["Poems"])
    else:
            return redirect(url_for('app.login'))


@app.route('/view/poem/<int:id>', methods = ['GET'])
def view_poem(id):
    api_url = f'{current_app.config["API_URL"]}/poems/{id}'
    headers = {"Content-Type": "application/json"}
    response = requests.get(api_url, headers = headers)
    print(response.status_code)
    print(response.text)
    poem = json.loads(response.text)
    print (poem)
    return render_template('view_poem.html', poem = poem)

@app.route('/logout')
def logout():
    req = make_response(redirect(url_for('app.index')))
    req.delete_cookie("access_token")
    req.delete_cookie("id")
    return req


@app.route('/create/poem', methods = ['GET', 'POST'])
def create_poem():
    jwt = request.cookies.get('access_token')

    if jwt:
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            print(title, body)
            user_id = request.cookies.get('id')
            print(user_id)
            data = {"title": title, "body": body, "user_id": user_id}
            print(data)
            headers = {"Content-Type": "application/json", "Authorization": f"Bearer{jwt}"}
            if title != "" and body != "":
                response = requests.post(f'{current_app.config["API_URL"]}/poems', data = data, headers = headers)
                print(response)
                if response.ok:
                    response = json.loads(response.text)
                    return redirect(url_for('app.view_poem', id = response['id'], jwt=jwt))
                else:
                    return redirect(url_for('app.create_poem'))
            else:
                return redirect(url_for('app.create_poem'))
        else:
            return redirect(url_for('update.html', jwt=jwt))
    else:
        return redirect(url_for('app.login'))
    

@app.route('/poem/<int:id>/delete')
def delete_poem(id):
    if request.cookies.get('access_token'):
        headers = {"Content-Type": "application/json"}
        response = requests.delete(api_url, headers = headers)
        print(response.status_code)
        print(response.text)
        return response