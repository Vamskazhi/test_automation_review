# Реализовать функцию для "разворачивания" вложенного списка в плоский.
# Описание: Написание кастомного исключения и тестирование его.

import copy
from typing import Any, Optional, Union

from src.exceptions import IsContainerType
from src.utils import is_сontainer


def make_list_flatten(
    nested_list: list[Any], result: Optional[Any] = None
) -> list[Union[int, float, str]]:
    if result is None:
        result = []
    if not isinstance(nested_list, list):
        raise IsContainerType(f"Unexpected type: {type(nested_list).__name__}")
    for i in nested_list:
        if isinstance(i, list):
            copy_result = copy.deepcopy(result)
            copy_result.append(make_list_flatten(i, result))
        elif is_сontainer(i):
            raise IsContainerType(
                f"Unexpected type: {type(i).__name__} only lists are supported"
            )
        else:
            result.append(i)
    return result
