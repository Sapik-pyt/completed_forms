import re
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


class ValidForm:
    """
    Класс для проверки валидности данных полученных при POST-запросе.
    """

    @staticmethod
    def validate_check_email(val: str):
        try:
            validate_email(val)
            return True
        except ValidationError:
            return False

    @staticmethod
    def validate_check_phone(val: str):
        return re.match(
            r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?'
            r'[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
            val, re.X
        )

    @staticmethod
    def validate_check_date(val: str):
        try:
            return datetime.strptime(val, '%Y.%m.%d').date() is not None
        except ValueError:
            return False


class FieldTypes:

    FIELDTYPES: dict = {
        'email': "email",
        'phone': "phone",
        'date': "date",
        'text': "text"
    }

    @staticmethod
    def get_type(field_value: str):
        if ValidForm.validate_check_date(field_value):
            return FieldTypes.FIELDTYPES['date']

        elif ValidForm.validate_check_phone(field_value):
            return FieldTypes.FIELDTYPES['phone']

        elif ValidForm.validate_check_email(field_value):
            return FieldTypes.FIELDTYPES['email']

        else:
            return FieldTypes.FIELDTYPES['text']


def take_forms(db, request):
    """
    Поиск подходящих форм из БД.
    """

    if request == {}:
        pass
    else:
        stack = []

        keys_request = set(request.keys())

        values_request = set(request.values())
        print(request)
        print(db)
        for item in range(len(db)):
            keys_db = set([*db[item].keys()][1:])
            val_db = set([*db[item].values()][1:])
            if (
                len(keys_db & keys_request) >= len(keys_db)
                    and len(val_db & values_request) >= len(val_db)
                    and 'name' == [*db[item]][0]):

                stack.append(db[item]['name'])
        print(stack)
        return stack
