from python_pytest.make_list_flatten import make_list_flatten, IsContainerType
import pytest


@pytest.mark.parametrize('checked_list', [
    [],
    [i for i in range(10)],
    [1, [], 2, [3], [4, 5, [6]]],
    ['test0', ['test2', ['test2']]],
],
                         ids=[
                             "empty",
                             "flat list of ints",
                             "nested ints (mixed depth)",
                             "nested strings (mixed depth)"
                         ]
)
def test_make_list_flatten_success(checked_list):
    for i in make_list_flatten(checked_list):
        assert type(i) != list, f"#{checked_list} has nested list"


@pytest.mark.parametrize('checked_list, expected_message', [
    (None, "Unexpected type: NoneType"),
    ([(x for x in range(33))], "Unexpected type: generator only lists are supported"),
    ([('tuple0', ('tuple1',))], "Unexpected type: tuple only lists are supported"),
    ([{x: x*2 for x in range(10)}], "Unexpected type: dict only lists are supported")
],
                         ids=[
                             'None input',
                             'Generator inside list',
                             'Tuple inside list',
                             'Dict inside list'
                         ]
)
def test_custom_exception(checked_list, expected_message):
    with pytest.raises(IsContainerType, match=expected_message):
        make_list_flatten(checked_list)