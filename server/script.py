import requests


LOCALHOST = 'http://127.0.0.1:8080'
FIELDS_FOR_FIND = [
    {
        'new_email': 'qwert@gmail.com',
        'first_email': 'poiuy@mail.ru',
        'user_phone': '8 999 444 42 42'
    },

    {
        'new_email_user': 'gfdgfd@gmail.com',
        'email_second': 'popeeqw@mail.ru',
        'first_name': 'Pavel'
    },

    {
        'new_email': 'edsad@gmail.com',
        'email': 'email@mail.ru',
        'first_name': 'Michal',
        'date': '2021.10.12'
    },

    {},

    {
        'email': 'first@gmail.com',
        'text': 'Hello, World',
        'phone': '8 800 555 35 35',
        'date': '1999.12.18',
        'user_name': 'text'
    }
]


def get_form(field):
    """
    Отправка POST запроса на получение списка подходящих форм.
    """
    print(field)
    res = requests.post(f'{LOCALHOST}/get_form/', data=field)
    print(res.content.decode('utf-8'))


if __name__ == '__main__':
    response = requests.get(LOCALHOST)

    if response.status_code == 200:

        print(
            'Получения списка всех шаблонов из БД.',
            response.content.decode('utf-8').replace('</br>', '\n'),
            'Направляем POST-запрос',
            sep='\n'
        )

        for n in range(len(FIELDS_FOR_FIND)):
            print(f'\n№{n+1}')
            get_form(FIELDS_FOR_FIND[n])
    else:
        print('В настоящее время сервер не доступен!')
