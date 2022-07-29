from Class import Spreadsheet, TooManyNumbersError
import pytest


def test_empty_init():
    spreadsheet = Spreadsheet()
    assert spreadsheet._number_of_columns == 15
    assert spreadsheet._number_of_rows == 15
    assert len(spreadsheet._constans_dict) == 0
    assert len(spreadsheet._function_dict) == 0


def test_init():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(10, 9, dict1, dict2)
    assert spreadsheet._number_of_rows == 9
    assert spreadsheet._number_of_columns == 10
    assert spreadsheet._function_dict == dict2
    assert spreadsheet._constans_dict == dict1


def test_new_int_value_if_cell_is_empy():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    spreadcheet = Spreadsheet(10, 10, dict1)
    spreadcheet.new_value('A2', 10)
    assert spreadcheet._constans_dict['A1'] == 5
    assert 'A2' in spreadcheet._constans_dict
    assert spreadcheet._constans_dict['A2'] == 10


def test_new_int_value():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    spreadcheet = Spreadsheet(10, 10, dict1)
    spreadcheet.new_value('A6', 5)
    assert spreadcheet._constans_dict['A6'] == 5


def test_new_str_value_if_cell_is_empty():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    spreadcheet = Spreadsheet(10, 10, dict1)
    spreadcheet.new_value('B6', 'New_value')
    assert spreadcheet._constans_dict['B6'] == 'New_value'


def test_new_str_value():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    spreadcheet = Spreadsheet(10, 10, dict1)
    spreadcheet.new_value('A8', 'New_value')
    assert spreadcheet._constans_dict['A8'] == 'New_value'


def test_set_function_to_add():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_add('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == '+'


def test_change_function_to_add():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_add('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '+'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A5']


def test_change_to_add_without_cells():
    dict2 = {
        'A1': ['avg']
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_add('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '+'


def test_set_function_to_min():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_min('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == 'min'


def test_set_function_to_min_empty_cells():
    dict2 = {
        'Z5': ['avg']
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_min('Z5')
    assert 'Z5' in spreadsheet._function_dict
    assert spreadsheet._function_dict['Z5'][0] == 'min'


def test_change_function_to_min():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_min('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'min'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A5']


def test_set_function_to_max():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_max('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == 'max'


def test_set_function_to_max_empty_cells():
    dict2 = {
        'Z5': ['avg']
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_max('Z5')
    assert 'Z5' in spreadsheet._function_dict
    assert spreadsheet._function_dict['Z5'][0] == 'max'


def test_change_function_to_max():
    dict2 = {
        'A1': ['avg', ['A1', 'A5', 'C8']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_max('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'max'
    assert spreadsheet._function_dict['A1'][1] == ['A1', 'A5', 'C8']


def test_set_function_to_multiplication():
    dict2 = {
        'A1': ['min', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_multiplication('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == '*'


def test_change_function_to_multiplication():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_multiplication('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '*'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A5']


def test_set_function_to_substraction():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_substract('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == '-'


def test_change_function_to_substraction():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_substract('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '-'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A5']


def test_set_function_to_division():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_division('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == '/'


def test_change_function_to_divison():
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_division('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '/'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A5']


def test_change_function_to_divison_empty():
    dict2 = {
        'A1': ['avg']
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_division('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == '/'


def test_set_function_to_avg():
    dict2 = {
        'A1': ['-', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_average('A4')
    assert 'A4' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A4'][0] == 'avg'


def test_change_to_avg():
    dict1 = {"A1": ["+"], "A2": ["+", ["A4", "B3", "B5"]]}
    spreadsheet = Spreadsheet(function_dict=dict1)
    spreadsheet.set_function_to_average('A2')
    assert spreadsheet._function_dict['A2'][0] == 'avg'
    assert spreadsheet._function_dict['A2'][1] == ['A4', 'B3', 'B5']


def test_change_function_to_average():
    dict2 = {
        'A1': ['+', ['A3']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.set_function_to_average('A1')
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'avg'
    assert spreadsheet._function_dict['A1'][1] == ['A3']


def test_assign_cells_list_to_function_celll():
    dict2 = {
        'A1': ['avg']
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.assign_cells_to_function('A1', ['A7', 'B7'])
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'avg'
    assert spreadsheet._function_dict['A1'][1] == ['A7', 'B7']


def test_assign_cells_list_to_function_cell():
    dict2 = {
        'A1': ['avg', ['A2']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.assign_cells_to_function('A1', ['A7', 'B7'])
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'avg'
    assert spreadsheet._function_dict['A1'][1] == ['A2', 'A7', 'B7']


def test_assign_cell_to_function_celll():
    dict2 = {
        'A1': ['avg', ['A3']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.assign_cells_to_function('A1', ['A7', 'B7'])
    assert 'A1' in spreadsheet._function_dict
    assert spreadsheet._function_dict['A1'][0] == 'avg'
    assert spreadsheet._function_dict['A1'][1] == ['A3', 'A7', 'B7']


def test_assign_cells_to_not_function_cell_error():
    with pytest.raises(KeyError):
        dict1 = {'A1': 5, 'A6': 10, 'A8': 11}
        spreadcheet = Spreadsheet(10, 10, dict1)
        spreadcheet.assign_cells_to_function('A1', ['A3', 'A5'])


def test_deactivate_function():
    dict2 = {
        'A1': ['-', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(function_dict=dict2)
    spreadsheet.deactivate_function('A1')
    assert len(spreadsheet._function_dict) == 0
    assert 'A1' not in spreadsheet._function_dict


def test_deactivate_function_error():
    with pytest.raises(KeyError):
        dict2 = {
            'A1': ['-', ['A3', 'A5']]
        }
        spreadsheet = Spreadsheet(function_dict=dict2)
        spreadsheet.deactivate_function('A2')


def test_save_to_file_as_json():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(10, 9, dict1, dict2)
    spreadsheet.save_to_file_as_json('test.json')


def test_save_file_without_json():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(10, 9, dict1, dict2)
    spreadsheet.save_to_file_as_json('test2')


def test_load_from_json_file():
    spreadsheet = Spreadsheet()
    spreadsheet.load_file_json('test.json')
    assert spreadsheet._number_of_columns == 10
    assert spreadsheet._number_of_rows == 9
    assert spreadsheet._function_dict['A1'] == ['avg', ['A3', 'A5']]


def test_save_and_load():
    dict1 = {
        'A1': 5,
        'A6': 10,
        'A8': 11
        }
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(10, 9, dict1, dict2)
    spreadsheet.save_to_file_as_json('test3')
    spreadsheet2 = Spreadsheet()
    spreadsheet2.load_file_json('test3.json')
    assert spreadsheet2._function_dict == dict2
    assert spreadsheet2._constans_dict == dict1
    assert spreadsheet2._number_of_columns == 10
    assert spreadsheet2._number_of_rows == 9


def test_load_change_and_save():
    dict1 = {
        'A1': 10,
        'H6': 4,
        'D8': 1,
        'F3': 34,
        'J4': 2,
        'H9': 3
        }
    dict2 = {
        'A1': ['avg', ['A3', 'A5']],
        'G7': ['min', ['A5', 'H9', 'F3']]
    }
    spreadsheet = Spreadsheet(9, 9, dict1, dict2)
    spreadsheet.save_to_file_as_json('test4')
    spreadsheet2 = Spreadsheet()
    spreadsheet2.load_file_json('test4.json')
    spreadsheet2._number_of_rows = 6
    spreadsheet2._number_of_columns = 6
    spreadsheet2.deactivate_function('A1')
    spreadsheet2.save_to_file_as_json('test5.json')
    spreadsheet3 = Spreadsheet()
    spreadsheet3.load_file_json('test5.json')
    assert spreadsheet3._number_of_columns == 6
    assert spreadsheet3._number_of_rows == 6
    assert len(spreadsheet3._function_dict) == 1
    assert len(spreadsheet3._constans_dict) == 5


def test_average():
    dict1 = {
        'A1': 10,
        'H6': 4,
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.average('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 5


def test_avg_with_str():
    dict1 = {
        'A1': 10,
        'H6': 5,
        'D8': 'Przyklad'
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.average('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 5


def test_set_cell_to_avg_and_avg():
    dict1 = {'A3': 2, 'A5': 8}
    dict2 = {
        'A1': ['avg', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    cells_list = spreadsheet._function_dict['A1'][1]
    spreadsheet.average('A1', cells_list)
    assert spreadsheet._constans_dict['A1'] == 5


def test_avg_with_empty_cells():
    dict1 = {
        'A1': 10,
        'H6': 4,
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8', 'B5']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.average('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 3.75


def test_min():
    dict1 = {
        'A1': 10,
        'H6': 4,
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.min('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 1


def test_min_with_str():
    dict1 = {
        'A1': 10,
        'H6': 'Przyklad2',
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.min('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 1


def test_set_cell_to_min_and_min():
    dict1 = {'A3': 2, 'A5': 8}
    dict2 = {
        'A1': ['min', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    cells_list = spreadsheet._function_dict['A1'][1]
    spreadsheet.min('A1', cells_list)
    assert spreadsheet._constans_dict['A1'] == 2


def test_max():
    dict1 = {
        'A1': 10,
        'H6': 4,
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.max('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 10


def test_max_with_str():
    dict1 = {
        'A1': 10,
        'H6': 'Przyklad 3',
        'D8': 1
        }
    cells_list = ['A1', 'H6', 'D8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.max('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 10


def test_max2():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    cells_list = ['A1', 'I6']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.max('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 120


def test_add():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    cells_list = ['A1', 'Z6', 'I8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.add('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 245


def test_add_with_str():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 'Przyklad4'
        }
    cells_list = ['A1', 'Z6', 'I8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.add('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 244


def test_add_empty_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    cells_list = ['A1', 'Z6', 'I8', 'D5']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.add('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 245


def test_substraction():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.subtraction('I8', 'Z6', 'A1')
    assert spreadsheet._constans_dict['I8'] == 4


def test_substraction_with_str():
    with pytest.raises(TypeError):
        dict1 = {
            'A1': 'Przyklad4',
            'Z6': 124,
            'I8': 1
            }
        spreadsheet = Spreadsheet(constans_dict=dict1)
        spreadsheet.subtraction('I8', 'Z6', 'A1')


def test_substraction_negative_difference():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.subtraction('I8', 'A1', 'Z6')
    assert spreadsheet._constans_dict['I8'] == -4


def test_set_and_substraction():
    dict1 = {'A3': 2, 'A5': 8}
    dict2 = {
        'A1': ['-', ['A3', 'A5']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    minued_cell = spreadsheet._function_dict['A1'][1][0]
    substrahend_cell = spreadsheet._function_dict['A1'][1][1]
    spreadsheet.subtraction('A1', minued_cell, substrahend_cell)
    assert spreadsheet._constans_dict['A1'] == -6


def test_substract_empty_cell():
    with pytest.raises(KeyError):
        spreadsheet = Spreadsheet()
        spreadsheet.subtraction('A1', 'A3', 'A3')


def test_multiplication():
    dict1 = {
        'A1': 2,
        'Z6': 9,
        'I8': 2
        }
    cells_list = ['A1', 'Z6', 'I8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.multiplication('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 36


def test_multiplication_with_str():
    dict1 = {
        'A1': 2,
        'Z6': 9,
        'I8': 'Przyklad5'
        }
    cells_list = ['A1', 'Z6', 'I8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.multiplication('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 18


def test_negative_multiplication():
    dict1 = {
        'A1': -2,
        'Z6': 9,
        'I8': 2
        }
    cells_list = ['A1', 'Z6', 'I8']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.multiplication('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == -36


def test_multiplication_with_empty_cell():
    dict1 = {
        'A1': -2,
        'Z6': 9,
        'I8': 2
        }
    cells_list = ['A1', 'Z6', 'I8', 'O7']
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.multiplication('A2', cells_list)
    assert spreadsheet._constans_dict['A2'] == 0


def test_division():
    dict1 = {
        'A1': 120,
        'Z6': 240,
        'I8': 1
        }
    spreadsheet = Spreadsheet(constans_dict=dict1)
    spreadsheet.division('I8', 'Z6', 'A1')
    assert spreadsheet._constans_dict['I8'] == 2


def test_division_with_str():
    with pytest.raises(TypeError):
        dict1 = {
            'A1': 'Przyklad6',
            'Z6': 240,
            'I8': 1
            }
        spreadsheet = Spreadsheet(constans_dict=dict1)
        spreadsheet.division('I8', 'Z6', 'A1')


def test_empty_cell_division():
    with pytest.raises(KeyError):
        spreadsheet = Spreadsheet()
        spreadsheet.division('A1', 'S2', 'D3')


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        dict = {'A1': 0, 'B2': 9}
        spreadsheet = Spreadsheet(constans_dict=dict)
        spreadsheet.division('A2', 'B2', 'A1')


def test_negative_division():
    dict = {'A1': -1, 'B2': 9}
    spreadsheet = Spreadsheet(constans_dict=dict)
    spreadsheet.division('A2', 'B2', 'A1')
    assert spreadsheet._constans_dict['A2'] == -9


def test_zero_division():
    dict = {'A1': -1, 'B2': 0}
    spreadsheet = Spreadsheet(constans_dict=dict)
    spreadsheet.division('A2', 'B2', 'A1')
    assert spreadsheet._constans_dict['A2'] == 0


def test_cell_calculate_add():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    dict2 = {
        'A2': ['+', ['A1', 'I8']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 121


def test_cell_calculate_change():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    dict2 = {
        'A2': ['+', ['A1', 'I8']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 121
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 3


def test_cell_calculate_add_no_cells():
    dict1 = {
        'A1': 120,
        'A2': 2,
        'Z6': 124,
        'I8': 1
        }
    dict2 = {
        'A2': ['+']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 2
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 2


def test_cell_calculate_substract_change_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 1
        }
    dict2 = {
        'A2': ['-', ['A1', 'I8']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 119
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 1


def test_cell_calculate_substract_with_empty_file():
    dict1 = {
        'A1': 120,
        'A2': 2,
        'Z6': 124,
        'I8': 1
        }
    dict2 = {
        'A2': ['-']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 2
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 2


def test_cell_calculate_substract_error():
    with pytest.raises(TooManyNumbersError):
        dict1 = {
            'A1': 120,
            'Z6': 124,
            'I8': 1
            }
        dict2 = {
            'A2': ['-', ['A1', 'I8', 'Z6']]
        }
        spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
        spreadsheet.cell_calculate()


def test_cell_calculate_division():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['/', ['A1', 'I8']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 60
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 1


def test_cell_calculate_division_Error():
    with pytest.raises(TooManyNumbersError):
        dict1 = {
            'A1': 120,
            'Z6': 124,
            'I8': 2
            }
        dict2 = {
            'A2': ['/', ['A1', 'I8', 'P8']]
        }
        spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
        spreadsheet.cell_calculate()


def test_cell_calculate_error():
    with pytest.raises(ValueError):
        dict1 = {
            'A1': 120,
            'Z6': 124,
            'I8': 2
            }
        dict2 = {
            'A2': ['/', ['A1']]
        }
        spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
        spreadsheet.cell_calculate()


def test_cell_calculate_multiplication():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*', ['A1', 'I8', 'Z6']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 29760
    spreadsheet.new_value('A1', 2)
    spreadsheet.cell_calculate()
    assert spreadsheet._constans_dict['A2'] == 496


def test_dependent_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*', ['A1', 'I8', 'Z6']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.new_dependent_cell('A2', 'A6')
    assert 'A6' in spreadsheet._function_dict['A2'][1]


def test_add_single_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {'A2': ['*']}
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.new_dependent_cell('A2', 'A6')
    assert spreadsheet._function_dict['A2'] == ['*', ['A6']]


def test_dependent_cell_add_same_cell():
    with pytest.raises(ValueError):
        dict1 = {
            'A1': 120,
            'Z6': 124,
            'I8': 2
            }
        dict2 = {
            'A2': ['*', ['A1', 'A6', 'Z6']]
        }
        spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
        spreadsheet.new_dependent_cell('A2', 'A6')


def test_add_dependent_cell_to_empy_dict():
    dict1 = {
            'A1': 120,
            'Z6': 124,
            'I8': 2
            }
    dict2 = {
        'A2': ['*']
        }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.new_dependent_cell('A2', 'A6')


def test_remove_dependent_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*', ['A1', 'A6', 'Z6']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.remove_dependent_cell('A2', 'A6')
    assert 'A6' not in spreadsheet._function_dict['A2'][1]


def test_remove_dependent_cell_empty():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.remove_dependent_cell('A2', 'A6')
    assert 'A6' not in spreadsheet._function_dict['A2']


def test_remove_constans_value():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.remove_constans_value('A1')
    assert 'A1' not in spreadsheet._constans_dict


def test_remove_constans_value_empty():
    dict1 = {
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    spreadsheet.remove_constans_value('A1')
    assert 'A1' not in spreadsheet._constans_dict


def test_show_cells_asigned_to_cell_none():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*']
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    cond = spreadsheet.show_cells_assigned_to_function_cell('A2')
    assert cond is None


def test_show_cells_assigned_to_cell():
    dict1 = {
        'A1': 120,
        'Z6': 124,
        'I8': 2
        }
    dict2 = {
        'A2': ['*', ['A1', 'Z6', 'I8']]
    }
    spreadsheet = Spreadsheet(constans_dict=dict1, function_dict=dict2)
    cond = spreadsheet.show_cells_assigned_to_function_cell('A2')
    assert cond == ['A1', 'Z6', 'I8']
