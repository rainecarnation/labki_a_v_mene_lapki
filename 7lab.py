from flask import Flask
from flask import request
import requests


app = Flask(__name__)


def format_information(data: dict) -> str:
    page = f"""
        <html>
            <head>
                <title>{data['email']}</title>
            </head>
            <body>
                <h1>{data['surname']} {data['name']}</h1>
                <h2>{data['birthday']}</h2>
                <img src="{data['image']}">
            </body>
        </html>
    """
    return page


login_page = """
<form action="/" method="post">
  <label for="login">LOGIN:</label>
  <input type="text" id="login" name="login"><br><br>
  <label for="lname">PASSWORD:</label>
  <input type="password" id="password" name="password"><br><br>
  <input type="submit" value="Submit">
</form>"""


@app.route('/', methods=["POST"])
def making_something(): 
    ksu_login = request.form['login']
    ksu_password = request.form['password']

    auth = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
         'username': ksu_login,
         'password': ksu_password
     })
     if not auth.ok:
         print(f"Помилка аутентифікації. Код:{auth.status_code} {auth.text}")
         auth.raise_for_status()
     else:
         print(f"Аутентификація успішна. Код:{auth.status_code}")
     auth_cookie = auth.cookies.get_dict()["JWT"]
     response = requests.get(url="https://ksu24.kspu.edu/api/v2/my/profile/", cookies={'JWT': auth_cookie})
     data = response.json()
    return format_profile(data)


@app.route('/', methods=["GET"])
def login():  
    return login_page


if __name__ == '__main__':
    app.run()
