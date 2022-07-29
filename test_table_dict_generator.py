from table_dict_generator import generate_dict


def test_numbers_between_0_25():
    dict = generate_dict(26)
    assert dict[0] == 'A'
    assert dict[22] == 'W'
    assert dict[25] == 'Z'


def test_numbers_more_than_25():
    dict = generate_dict(45)
    assert dict[26] == 'Aa'
    assert dict[30] == 'Ae'
    assert dict[44] == 'As'
