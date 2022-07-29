from Class import Spreadsheet, NoFileError
import argparse
import sys


def main(arguments):
    parser = argparse.ArgumentParser()
    parser.add_argument('-file', help='Name_json_file')
    parser.add_argument('-columns', help='Number of columns')
    parser.add_argument('-rows', help='Number of rows')
    parser.add_argument('-Empty_spreadsheet', action='store_true',
                        help='Create_empty_spreadsheet')
    parser.add_argument('-save',
                        help="""if you want to save changes in empty spreadsheet
                        example = -save 'name_file_you_want_save''""")
    parser.add_argument('-dont_save', action='store_true',
                        help="""by default all changes are saved
                        if dont_save is on all changes wont be saved""")
    parser.add_argument('-set_cell_to_avg',
                        help="cell")
    parser.add_argument('-set_cell_to_min',
                        help="cell")
    parser.add_argument('-set_cell_to_max',
                        help="cell'")
    parser.add_argument('-set_cell_to_add',
                        help="cell'")
    parser.add_argument('-set_cell_to_substract',
                        help="cell'")
    parser.add_argument('-set_cell_to_division',
                        help="cell'")
    parser.add_argument('-set_cell_to_multiplication',
                        help="cell")
    parser.add_argument('-cells_list',
                        help="""assign cell list to function cell,
                        first cell have to be function cell
                        example = A3[A2,A5,A7]""")
    parser.add_argument('-add_cell',
                        help="""assign cell to functionc cell
                        example = 'A3,A5'""")
    parser.add_argument('-remove_cell',
                        help=""" remove cell from funcion cell list
                        example = 'A2, A4'""")
    parser.add_argument('-New_constans_value',
                        help="for example 'A3, 5'")
    parser.add_argument('-show_cells',
                        help='Printing cells assigned to function cell')
    parser.add_argument('-deactivate_function',
                        help="""deactivating fucntion cell""")
    parser.add_argument('-remove_value',
                        help='Remove constans value from cell')
    args = parser.parse_args(arguments[1:])
    spreadsheet = Spreadsheet()
    if not args.Empty_spreadsheet:
        if not args.file:
            raise NoFileError("""If you dont switch on
                                '-Empty_spreadsheet' you have to give file""")
        else:
            spreadsheet.load_file_json(args.file)
    if args.rows:
        spreadsheet._number_of_rows = int(args.rows)
    if args.columns:
        spreadsheet._number_of_columns = int(args.columns)
    if args.set_cell_to_avg:
        cell = args.set_cell_to_avg
        spreadsheet.set_function_to_average(cell)
    if args.set_cell_to_min:
        cell = args.set_cell_to_min
        spreadsheet.set_function_to_min(cell)
    if args.set_cell_to_max:
        cell = args.set_cell_to_max
        spreadsheet.set_function_to_max(cell)
    if args.set_cell_to_add:
        cell = args.set_cell_to_add
        spreadsheet.set_function_to_add(cell)
    if args.set_cell_to_substract:
        cell = args.set_cell_to_substract
        spreadsheet.set_function_to_substract(cell)
    if args.set_cell_to_division:
        cell = args.set_cell_to_division
        spreadsheet.set_function_to_division(cell)
    if args.set_cell_to_multiplication:
        cell = args.set_cell_to_multiplication
        spreadsheet.set_function_to_multiplication(cell)
    if args.New_constans_value:
        cell_and_value = args.New_constans_value
        try:
            tokens = cell_and_value.split(',')
            cell = tokens[0]
            new_value = tokens[1]
        except IndexError:
            raise IndexError('Two cell needed')
        try:
            new_value = int(new_value)
            spreadsheet.new_value(cell, new_value)
        except ValueError:
            spreadsheet.new_value(cell, new_value)
    if args.remove_value:
        cell = args.remove_value
        spreadsheet.remove_constans_value(cell)
    if args.cells_list:
        cells_list = []
        cells = args.cells_list
        cells = cells.split(',')
        value_cell = cells[0]
        for cell in cells[1:]:
            if '[' in cell:
                cell = cell[1:]
            if ']' in cell:
                cell = cell[:-1]
            cells_list.append(cell)
        spreadsheet.assign_cells_to_function(value_cell, cells_list)
    if args.add_cell:
        try:
            tokens = args.add_cell.split(",")
            cell = tokens[0]
            dependent_cell = tokens[1]
            spreadsheet.new_dependent_cell(cell, dependent_cell)
        except IndexError:
            raise IndexError('Two cells needed')
    if args.deactivate_function:
        spreadsheet.deactivate_function(args.deactivate_function)
    if args.remove_cell:
        tokens = args.remove_cell.split(",")
        cell = tokens[0]
        removed_cell = tokens[1]
        spreadsheet.remove_dependent_cell(cell, removed_cell)
    spreadsheet.cell_calculate()
    if not args.dont_save:
        if args.file:
            spreadsheet.save_to_file_as_json(args.file)
        if args.Empty_spreadsheet:
            if args.save:
                spreadsheet.save_to_file_as_json(args.save)
    if args.show_cells:
        cell = args.show_cells
        print(spreadsheet.show_cells_assigned_to_function_cell(cell))
    else:
        print(spreadsheet)


if __name__ == '__main__':
    main(sys.argv)
