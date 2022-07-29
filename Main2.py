import argparse
import sys
from Class import NoFileError, Spreadsheet


def create_empty_spreadsheet(spreadsheet, args):
    spreadsheet = Spreadsheet()
    return spreadsheet


def spreadsheet_size(spreadsheet, args):
    columns = int(args.columns)
    rows = int(args.rows)
    dict1 = spreadsheet._constans_dict
    dict2 = spreadsheet._function_dict
    return Spreadsheet(columns, rows, dict1, dict2)


def function_assign(args, spreadsheet):
    rows = spreadsheet._number_of_rows
    columns = spreadsheet._number_of_columns
    dict1 = spreadsheet._constans_dict
    dict2 = spreadsheet._function_dict
    spreadsheet = Spreadsheet(columns, rows, dict1, dict2)
    if args.add:
        cell = args.add
        spreadsheet.set_function_to_add(cell)
    if args.min:
        cell = args.min
        spreadsheet.set_function_to_min(cell)
    if args.avg:
        cell = args.avg
        spreadsheet.set_function_to_average(cell)
    if args.substract:
        cell = args.substract
        spreadsheet.set_function_to_substract(cell)
    if args.division:
        cell = args.division
        spreadsheet.set_function_to_division(cell)
    if args.multiplication:
        cell = args.multiplication
        spreadsheet.set_function_to_multiplication(cell)
    if args.max:
        cell = args.max
        spreadsheet.set_function_to_max(cell)
    return spreadsheet


def Set_constans_value(args, spreadsheet):
    rows = spreadsheet._number_of_rows
    columns = spreadsheet._number_of_columns
    dict1 = spreadsheet._constans_dict
    dict2 = spreadsheet._function_dict
    spreadsheet = Spreadsheet(columns, rows, dict1, dict2)
    cell = args.cell
    try:
        new_value = int(args.value)
    except ValueError:
        new_value = args.value
    spreadsheet.new_value(cell, new_value)
    return spreadsheet


def assign_cells(args, spreadsheet):
    rows = spreadsheet._number_of_rows
    columns = spreadsheet._number_of_columns
    dict1 = spreadsheet._constans_dict
    dict2 = spreadsheet._function_dict
    spreadsheet = Spreadsheet(columns, rows, dict1, dict2)
    cell = args.cell
    if args.cells_list:
        cells_list = []
        list = args.cells_list.split(',')
        for cell1 in list:
            cells_list.append(cell1)
        spreadsheet.assign_cells_to_function(cell, cells_list)
    if args.single_cell:
        single_cell = args.single_cell
        spreadsheet.new_dependent_cell(cell, single_cell)
    return spreadsheet


def remove_cell_from_function_cell_list(args, spreadsheet):
    rows = spreadsheet._number_of_rows
    columns = spreadsheet._number_of_columns
    dict1 = spreadsheet._constans_dict
    dict2 = spreadsheet._function_dict
    spreadsheet = Spreadsheet(columns, rows, dict1, dict2)
    spreadsheet.remove_dependent_cell(args.function_cell, args.removed_cell)
    return spreadsheet


def show_assigned_cells(args, spreadsheet):
    function_cell = args.function_cell
    return(spreadsheet.show_cells_assigned_to_function_cell(function_cell))


def Main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help='It needs file name')
    parser.add_argument('-dont_save', action='store_true')
    parser.add_argument('-empty_spreadsheet', action='store_true')
    parser.add_argument('-save',
                        help="""If you want to save changes in empty spreadsheet
                        it needs file name""")
    parser.add_argument('-deactivate_function',
                        help="""deactivating function cell""")
    parser.add_argument('-remove_value',
                        help='Remove constans value from cell')
    subparsers = parser.add_subparsers()
    parser_size = subparsers.add_parser('size')
    parser_size.add_argument('rows')
    parser_size.add_argument('columns')
    parser_size.set_defaults(size_fun=spreadsheet_size)
    parser_function_set = subparsers.add_parser('function_set')
    parser_function_set.add_argument('-add',
                                     help="""Sets add function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-min',
                                     help="""Sets min function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-avg',
                                     help="""Sets average function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-substract',
                                     help="""Sets substract function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-division',
                                     help="""Sets division function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-multiplication',
                                     help="""Sets multiplication function to cell,
                                     needs cell """)
    parser_function_set.add_argument('-max',
                                     help="""Sets max function to cell,
                                     needs cell """)
    parser_function_set.set_defaults(set_fun=function_assign)
    parser_constans_set = subparsers.add_parser('new_value')
    parser_constans_set.add_argument('cell')
    parser_constans_set.add_argument('value')
    parser_constans_set.set_defaults(new_value=Set_constans_value)
    parser_assign_cell = subparsers.add_parser('assign_cell')
    parser_assign_cell.add_argument('cell')
    parser_assign_cell.add_argument('-cells_list',
                                    help="'it need cells connected by ','")
    parser_assign_cell.add_argument('-single_cell',
                                    help='you can add 1 cell to function cell')
    parser_assign_cell.set_defaults(set_cell=assign_cells)
    parser_remove_cell = subparsers.add_parser('remove_cell')
    parser_remove_cell.add_argument('function_cell',
                                    help="""function cell
                                            with function cells list""")
    parser_remove_cell.add_argument('removed_cell',
                                    help="""Cell you want to remove from
                                            function cell list""")
    parser_show_assigned_cell = subparsers.add_parser('show_assigned_cells')
    parser_show_assigned_cell.add_argument('function_cell')
    parser_show_assigned_cell.set_defaults(show=show_assigned_cells)
    parser_remove_cell.set_defaults(remove=remove_cell_from_function_cell_list)
    args = parser.parse_args(arguments[1:])
    spreadsheet = Spreadsheet()
    if not args.empty_spreadsheet:
        if not args.file:
            raise NoFileError('You have to add file')
        else:
            spreadsheet.load_file_json(args.file)
    if 'size_fun' in args:
        spreadsheet = args.size_fun(spreadsheet, args)
    if 'set_fun' in args:
        spreadsheet = args.set_fun(args, spreadsheet)
    if 'new_value' in args:
        spreadsheet = args.new_value(args, spreadsheet)
    if 'set_cell' in args:
        spreadsheet = args.set_cell(args, spreadsheet)
    if 'remove' in args:
        spreadsheet = args.remove(args, spreadsheet)
    spreadsheet.cell_calculate()
    if 'empty' in args:
        spreadsheet = args.empty(args, spreadsheet)
    if args.deactivate_function:
        cell = args.deactivate_function
        spreadsheet.deactivate_function(cell)
    if not args.dont_save:
        if not args.empty_spreadsheet:
            spreadsheet.save_to_file_as_json(args.file)
    if args.remove_value:
        cell = args.remove_value
        spreadsheet.remove_constans_value(cell)
    if args.empty_spreadsheet:
        if args.save:
            spreadsheet.save_to_file_as_json(args.save)
    if 'show' in args:
        print(args.show(args, spreadsheet))
    else:
        print(spreadsheet)


if __name__ == '__main__':
    Main(sys.argv)
