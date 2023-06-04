import requests


# Отримати кукі аутентифікації і використовувати її

def auth(login: str,
         password: str):
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={'username': login,
                                   'password': password})
    if response:
        print("Успіх.")
    else:
        print("Не вийшло. Спробуйте ще раз.")

    try:
        cookie = response.cookies.get_dict()["JWT"]
        return cookie
    except():
        print("Печиво скінчилось. Тепер ви на дієті.")
        return

#Обробити статус код

def get_value(url: str,
              cookie,
              key,
              filter_by: dict = None):
    response = requests.get(url=url,
                            cookies={'JWT': cookie})
    response.raise_for_status()
    # Перетворити на json
    data = response.json()
    for item in data.get('results',
                         [data]):
        if filter_by and item.get(list(filter_by.keys())[0]) != filter_by.get(list(filter_by.keys())[0]):
            continue
        if key in item:
            return item[key]

def get_info(url, cookie):
    response = requests.get(url=url,
                            cookies={'JWT': cookie})
    response.raise_for_status()

    data = response.json()
    results_list = data.get('results',
                            [data])
    for dictionary in results_list:
        for key, value in dictionary.items():
            print(f"{key}: {value}")
        print("-" * 10)
def main():
    login = input("Введіть логін - ")
    password = input("Введіть пароль: ")

    auth_student = auth(login=login, password=password)
    print("Запит на сервер")
    print("-" * 10)
    get_info(url="https://ksu24.kspu.edu/api/v2/my/profile/",
             cookie=auth_student)

    print("Відправляємо запит")
    get_info(url="https://ksu24.kspu.edu/api/v2/my/students/",
             cookie=auth_student)

main()
