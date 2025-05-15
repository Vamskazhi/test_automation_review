from typing import Any

from faker import Faker

fake = Faker()


def fake_call(method: str, *args: Any, **kwargs: Any) -> Any:
    return getattr(fake, method)(*args, **kwargs)


def created_dict(key: str, value: str, count: int = 4) -> dict[Any, Any]:
    return {fake_call(key): fake_call(value) for _ in range(count)}
