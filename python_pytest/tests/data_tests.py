from collections.abc import Iterable
from faker import Faker
import random

fake = Faker()


def fake_call(method: str, *args, **kwargs):
    return getattr(fake, method)(*args, **kwargs)


def created_dict(key, value, count=4) -> dict:
    return {
        fake_call(key): fake_call(value)
        for _ in range(count)
    }


def generate_dict(count=4):
    for _ in range(count):
        yield {
            fake.uuid4(): fake.name()
        }