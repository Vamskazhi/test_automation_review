from collections.abc import Iterable


def is_сontainer(obj) -> bool:
    return isinstance(obj, Iterable) and not isinstance(obj, str) and not isinstance(obj, list)


def all_of_type(obj, expected_type):
    return all(isinstance(x, expected_type) for x in obj)


def first(iterable, default=None):
    return next(iter(iterable), default)