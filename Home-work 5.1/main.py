import string
import keyword


def is_valid_variable_name(name):

    if name in keyword.kwlist:
        return False


    if name[0].isdigit():
        return False


    if name.count('_') > 1:
        return False


    allowed_chars = string.ascii_lowercase + string.digits + '_'
    for char in name:
        if char not in allowed_chars:
            return False

    return True



test_cases = [
    "_", "__", "___", "x", "get_value", "get value", "get!value",
    "some_super_puper_value", "Get_value", "get_Value", "getValue",
    "3m", "m3", "assert", "assert_exception"
]


for test in test_cases:
    print(f"{test} => {is_valid_variable_name(test)}")
