# Описание: Написать функцию для сортировки словаря по ключам и тесты для этой функции.
from python_pytest.tests.utils import all_of_type, first


class TypeKeysError(Exception):
    def __init__(self, message='Cannot sort dictionary: keys are of different types'):
        super().__init__(message)
        self.msgfmt = message


def sorted_dict_by_key(data: dict) -> dict:
    if not isinstance(data, dict):
        raise TypeKeysError(f'Cannot sort by key: type "{type(data).__name__}" does not contain keys')
    keys_dict = data.keys()
    if not all_of_type(keys_dict, type(first(keys_dict))):
        raise TypeKeysError
    return {key: data[key] for key in sorted(data)}

