# Описание: Написать функцию для сортировки словаря по ключам и
# тесты для этой функции.
from typing import Any

from src.exceptions import TypeKeysError
from src.utils import all_of_type, first


def sorted_dict_by_key(data: dict[Any, Any]) -> dict[Any, Any]:
    if not isinstance(data, dict):
        raise TypeKeysError(
            f'Cannot sort by key: type "{type(data).__name__}" '
            f"does not contain keys"
        )
    keys_dict = data.keys()
    if not all_of_type(keys_dict, type(first(keys_dict))):
        raise TypeKeysError
    return {key: data[key] for key in sorted(data)}
