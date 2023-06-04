import requests
import pandas as pd

# Отримати кукі аутентифікації і використовувати її

def auth(login: str,
         password: str):
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/",
                             data={'username': login,
                                   'password': password})
    if response:
        print("Успіх.")
    else:
        print("Не вийшло авторизуватись. Спробуйте ще раз.")

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

def get_json(url: str, auth_student):
    profile_request = requests.get(url=url,
                                   cookies={'JWT': auth_student})
    if profile_request.ok:
        print("Запит виконаний успішно")
        return profile_request.json()
    else:
        print(f"Помилка запиту. "
              f"Кoд:{profile_request.status_code}")
        profile_request.raise_for_status()
        return None

def create_plot(df: pd.DataFrame,
                key: str):
    try:
        df[key].plot(kind="barh",
                     title='Графік')
        plt.show()
    except():
        print("Помилка графіку")


def sort_data_frame(df, colums,
                    inplance=True,
                    ascending=False,
                    ignore_index=False,
                    key=None):
    return df.sort_values(by=colums,
                          inplace=inplance,
                          ascending=ascending,
                          ignore_index=ignore_index,
                          key=key)

def main():
    login = input("Логін: ")
    password = input("Пароль: ")

    auth_student = auth(login=login, password=password)

    student_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/", auth_student=auth_student, key="id")

    print("Запит на отмання журнала...")
    get_info(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
             auth_student=auth_student)
    recordbook_id = get_value(url="https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
                              auth_student=auth_student,
                              key="id")

    print("Запит на оцінки дисциплін")
    get_info(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_student=auth_student)

    data = get_json(
        url="https://ksu24.kspu.edu/api/v2/my/students/" + student_id + "/recordbooks/" + recordbook_id + "/records",
        auth_student=auth_student)

    if "results" in data.keys():
        results_list = data["results"]
        df = pd.DataFrame.from_records(results_list)
    else:
        df = pd.DataFrame(data)

    sort_data_frame(df, ["result"], 
                    ascending=True)
    df.to_excel("lab6.xlsx",
                sheet_name="Оцінки",
                index=False)
    create_plot(df,
                "result")


main()
