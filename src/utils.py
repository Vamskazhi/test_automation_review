from typing import Any, Optional
from typing import Iterable as Iterable_type
from collections.abc import Iterable


def is_сontainer(obj: Any) -> bool:
    return isinstance(obj, Iterable) and not isinstance(obj, str) \
        and not isinstance(obj, list)


def all_of_type(obj: Any, expected_type: type) -> bool:
    return all(isinstance(x, expected_type) for x in obj)


def first(iterable: Iterable_type[Any], default: Optional[Any] = None) -> \
        Optional[Any]:
    return next(iter(iterable), default)
