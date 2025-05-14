# type: ignore
import pytest
from tests.helpers.data_tests import fake_call, created_dict
from src.sort_dict import sorted_dict_by_key
from src.exceptions import TypeKeysError


@pytest.mark.parametrize('input_data', [
    {},
    {x*5: x for x in range(10)},
    created_dict('uuid4', 'name', 10),
    {(101, 1): fake_call('word'), (1, 2): fake_call('word'),
     (0,): fake_call('word')}
],
                         ids=[
                             'Empty dictionary',
                             'Integer keys',
                             'UUID4 keys',
                             'Tuple keys'
                         ]
)
def test_sorted_dict_by_key_success(input_data):
    keys_dict = list(sorted_dict_by_key(input_data).keys())
    assert keys_dict == sorted(keys_dict), f"Keys {keys_dict} unsorted!"


@pytest.mark.parametrize('input_data, expected_message', [
    (None, 'Cannot sort by key: type "NoneType" does not contain keys'),
    ([x for x in range(10)],
     'Cannot sort by key: type "list" does not contain keys'),
    (
            {(101, 1): fake_call('word'), fake_call('uuid4'): (0,)},
            'Cannot sort dictionary: keys are different types'
    ),
],
                         ids=[
                             'None input',
                             'List input',
                             'Mixed key types'
                         ]
)
def test_sorted_dict_by_key_negative(input_data, expected_message):
    with pytest.raises(TypeKeysError, match=expected_message):
        sorted_dict_by_key(input_data)
