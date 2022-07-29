from model_io import write_to_json, read_from_json
from table_dict_generator import generate_dict


class NoFileError(Exception):
    pass


class TooManyNumbersError(Exception):
    pass


class Spreadsheet:
    def __init__(self, number_of_columns=15, number_of_rows=15,
                 constans_dict=None, function_dict=None):
        self._number_of_columns = number_of_columns
        self._number_of_rows = number_of_rows
        if constans_dict is None:
            self._constans_dict = {}
        else:
            self._constans_dict = constans_dict
        if function_dict is None:
            self._function_dict = {}
        else:
            self._function_dict = function_dict

    def number_of_columns(self):
        return self._number_of_columns

    def number_of_rows(self):
        return self._number_of_rows

    def constans_dict(self):
        return self._constans_dict

    def function_dict(self):
        return self._function_dict

    def __str__(self):
        """ This method generate spreadsheet based on number of rows, columns,
            constans value dict and function dict
            and also print it into terminal."""
        alph_dict = generate_dict(self._number_of_columns)
        d = self._constans_dict
        x = self._number_of_columns + 1
        y = self._number_of_rows + 1
        table = ''
        for i in range(0, y):
            for u in range(0, x):
                if i == 0:
                    if u == 0:
                        table += '|       '
                    elif u == x-1:
                        if len(alph_dict[u-1]) == 1:
                            table += f'|   {alph_dict[u-1]}   |\n'
                        if len(alph_dict[u-1]) == 2:
                            table += f'|   {alph_dict[u-1]}  |\n'
                        if len(alph_dict[u-1]) == 3:
                            table += f'|  {alph_dict[u-1]}  |\n'
                        table += '--------'*x
                        table += '-'
                        table += '\n'
                    else:
                        if len(alph_dict[u-1]) == 1:
                            table += f'|   {alph_dict[u-1]}   '
                        if len(alph_dict[u-1]) == 2:
                            table += f'|   {alph_dict[u-1]}  '
                        if len(alph_dict[u-1]) == 3:
                            table += f'|  {alph_dict[u-1]}   '
                else:
                    if u == 0:
                        table += f'|  {i:<3}  '
                    else:
                        if (f'{alph_dict[u-1]}{i}') in d:
                            if u == x-1:
                                cell = f'{alph_dict[u-1]}{i}'
                                text = str(d[cell])
                                if len(text) > 7:
                                    text = text[:5]
                                    table += f'|{text}..|\n'
                                elif len(text) == 7:
                                    table += f'|{text}|\n'
                                elif len(text) == 6:
                                    table += f'| {text}|\n'
                                elif len(text) == 5:
                                    table += f'| {text} |\n'
                                elif len(text) == 4:
                                    table += f'|  {text} |\n'
                                else:
                                    table += f'|   {text:>3} |\n'
                                table += '--------'*x
                                table += '-'
                                table += '\n'
                            else:
                                cell = f'{alph_dict[u-1]}{i}'
                                text = str(d[cell])
                                if len(text) > 7:
                                    text = text[:5]
                                    table += f'|{text}..'
                                elif len(text) == 7:
                                    text = f'{text}'
                                    table += f'|{text}'
                                elif len(text) == 6:
                                    text = f' {text}'
                                    table += f'|{text}'
                                elif len(text) == 5:
                                    text = f'{text}'
                                    table += f'| {text} '
                                elif len(text) == 4:
                                    text = f'{text}'
                                    table += f'|  {text} '
                                else:
                                    table += f'|  {text:>3}  '
                        else:
                            if u == x-1:
                                table += "|       |\n"
                                table += '--------'*x
                                table += '-'
                                table += '\n'
                            else:
                                table += '|       '
        return table

    def new_value(self, cell, new_value):
        """
        args:
        cell: To this cell we want to assing new str or int constans value
        new_value: New value of cell
        """
        self._constans_dict[cell] = new_value

    def set_function_to_add(self, cell):
        """
        Assing addition function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['+']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['+']
        else:
            self._function_dict[cell] = ['+']

    def set_function_to_substract(self, cell):
        """
        Assing substraction function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['-']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['-']
        else:
            self._function_dict[cell] = ['-']

    def set_function_to_min(self, cell):
        """
        Assing min function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['min']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['min']
        else:
            self._function_dict[cell] = ['min']

    def set_function_to_max(self, cell):
        """
        Assing max function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['max']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['max']
        else:
            self._function_dict[cell] = ['max']

    def set_function_to_average(self, cell):
        """
        Assing average function to cell.
        """
        if cell not in self._function_dict:
            self._function_dict[cell] = ['avg']
        else:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['avg']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['avg']

    def set_function_to_division(self, cell):
        """
        Assing division function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['/']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['/']
        else:
            self._function_dict[cell] = ['/']

    def set_function_to_multiplication(self, cell):
        """
        Assing multiplication function to cell.
        """
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                cells_list = self._function_dict[cell][1]
                self._function_dict[cell] = ['*']
                list = self._function_dict[cell]
                list.append(cells_list)
            else:
                self._function_dict[cell] = ['*']
        else:
            self._function_dict[cell] = ['*']

    def assign_cells_to_function(self, cell, list_of_cells):
        """
        Assign cells list to functional cell.
        """
        try:
            if len(self._function_dict[cell]) > 1:
                list = self._function_dict[cell]
                function = self._function_dict[cell][0]
                cells_list = self._function_dict[cell][1]
                for cell in list_of_cells:
                    cells_list.append(cell)
                list.clear()
                list.append(function)
                list.append(cells_list)
            else:
                list = self._function_dict[cell]
                list.append(list_of_cells)
                self._function_dict[cell] = list
        except KeyError:
            raise KeyError('You cannot assign cells to not funcion cell')

    def deactivate_function(self, cell):
        """
        Remove function from cell.
        """
        try:
            self._function_dict.pop(cell)
            if cell in self._constans_dict:
                self._constans_dict.pop(cell)
        except KeyError:
            raise KeyError('You can deactivate only cells which has fucntion')

    def save_to_file_as_json(self, file_name):
        """
        This method saves file to json format.
        """
        dict = {}
        dict['constans_dict'] = self._constans_dict
        dict['function_dict'] = self._function_dict
        dict['number_of_columns'] = self._number_of_columns
        dict['number_of_rows'] = self._number_of_rows
        if 'json' in file_name:
            file_name = file_name
        else:
            file_name = f'{file_name}.json'
        with open(file_name, 'w') as jsonfp:
            write_to_json(jsonfp, dict)

    def load_file_json(self, file_handle):
        """
        This method load file and update number of rows, columns,
        constans dict and function dict
        """
        with open(file_handle) as fp:
            dict = read_from_json(fp)
        self._function_dict = dict['function_dict']
        self._constans_dict = dict['constans_dict']
        if dict['number_of_rows']:
            self._number_of_rows = dict['number_of_rows']
        else:
            self._number_of_rows = 15
        if dict['number_of_columns']:
            self._number_of_columns = dict['number_of_columns']
        else:
            self._number_of_columns = 15

    def average(self, cell_off_value, cells_list):
        """
        This method counts average of cells from cells_list
        and save it into cell_of_value
        """
        sum = 0
        for cell in cells_list:
            if cell in self._constans_dict:
                if type(self._constans_dict[cell]) == str:
                    pass
                else:
                    sum += self._constans_dict[cell]
        self._constans_dict[cell_off_value] = round(sum / len(cells_list), 2)

    def min(self, cell_of_value, cells_list):
        """
        This method counts min of cells from cells_list
        and save it into cell_of_value
        """
        value_list = []
        for cell in cells_list:
            if cell in self._constans_dict:
                try:
                    value = int(self._constans_dict[cell])
                    value_list.append(value)
                except ValueError:
                    pass
        value_list.sort()
        self._constans_dict[cell_of_value] = value_list[0]

    def max(self, cell_value, cells_list):
        """
        This method counts max of cells
        from cells_list and save it into cell_of_value
        """
        value_list = []
        for cell in cells_list:
            if cell in self._constans_dict:
                if type(self._constans_dict[cell]) == str:
                    pass
                else:
                    value_list.append(self._constans_dict[cell])
        value_list.sort()
        value_list = value_list[::-1]
        self._constans_dict[cell_value] = value_list[0]

    def add(self, cell_of_value, cells_list):
        """
        This method adds value of cells
        from cells_list and save it into cell_of_value
        """
        sum = 0
        for cell in cells_list:
            if cell in self._constans_dict:
                if type(self._constans_dict[cell]) == str:
                    pass
                else:
                    sum += self._constans_dict[cell]
        self._constans_dict[cell_of_value] = sum

    def subtraction(self, cell_value, minued_cell, substrahend_cell):
        """
        This method substract substrahend_cell and minued_cell and
        save the difference in cell_of_value
        """
        try:
            dict = self._constans_dict
            difference = dict[minued_cell] - dict[substrahend_cell]
            self._constans_dict[cell_value] = difference
        except KeyError:
            raise KeyError("Wrong cell format or cell doesn't have value")
        except TypeError:
            raise TypeError('Cannot make substraction operation on string')

    def multiplication(self, cell_value, list_of_cells):
        """
        This method multiplication value of cells from cells_list
        and save it into cell_of_value
        """
        product = 1
        for cell in list_of_cells:
            if cell in self._constans_dict:
                if type(self._constans_dict[cell]) == str:
                    pass
                else:
                    product *= self._constans_dict[cell]
            else:
                product *= 0
        self._constans_dict[cell_value] = product

    def division(self, cell_of_value, divident_cell, divisor_cell):
        """
        This method divide value of cells from cells_list
        and save it into cell_of_value
        """
        try:
            x = self._constans_dict[divident_cell]
            y = self._constans_dict[divisor_cell]
            fraction = round(x/y, 2)
        except ZeroDivisionError:
            raise ZeroDivisionError('Value of divisor cell cannot be 0')
        except KeyError:
            raise KeyError('You cannot divide empty cells')
        except TypeError:
            raise TypeError('Cannot make division operation on string type')
        self._constans_dict[cell_of_value] = fraction

    def cell_calculate(self):
        """
        This method is responsible for updating value in function cells
        if the value from dependent value changed
        """
        if (self._function_dict) != 0:
            for cell in self._function_dict:
                function = self._function_dict[cell][0]
                if len(self._function_dict[cell]) > 1:
                    cells_list = self._function_dict[cell][1]
                    if function == 'avg':
                        self.average(cell, cells_list)
                    if function == 'min':
                        self.min(cell, cells_list)
                    if function == 'max':
                        self.max(cell, cells_list)
                    if function == '-':
                        if len(cells_list) > 2:
                            raise TooManyNumbersError("""In this operation it can
                                                        be used max
                                                        two numbers.""")
                        else:
                            minued_cell = cells_list[0]
                            substrahend_cell = cells_list[1]
                            self.subtraction(cell, minued_cell,
                                             substrahend_cell)
                    if function == '+':
                        self.add(cell, cells_list)
                    if function == '/':
                        if len(cells_list) > 2:
                            raise TooManyNumbersError("""In this operation have to
                                                       get two numbers.""")
                        elif len(cells_list) < 2:
                            raise ValueError('Two numbers needed.')
                        else:
                            divident_cell = cells_list[0]
                            divider_cells = cells_list[1]
                            self.division(cell, divident_cell, divider_cells)
                    if function == '*':
                        self.multiplication(cell, cells_list)

    def new_dependent_cell(self, cell, dependent_cell):
        if len(self._function_dict[cell]) == 0:
            list = []
            list.append(dependent_cell)
            self.assign_cells_to_function(cell, list)
        elif len(self._function_dict[cell]) == 1:
            list = []
            list.append(dependent_cell)
            self.assign_cells_to_function(cell, list)
        else:
            cells_list = self._function_dict[cell][1]
            if dependent_cell in cells_list:
                raise ValueError('Cell is already added to dependent cells')
            else:
                cells_list.append(dependent_cell)

    def remove_dependent_cell(self, cell, dependent_cell):
        if len(self._function_dict[cell]) == 0:
            pass
        if len(self._function_dict[cell]) == 1:
            pass
        else:
            cells_list = self._function_dict[cell][1]
            cells_list.remove(dependent_cell)

    def remove_constans_value(self, cell):
        if cell in self._constans_dict:
            self._constans_dict.pop(cell)
        else:
            pass

    def show_cells_assigned_to_function_cell(self, cell):
        if cell in self._function_dict:
            if len(self._function_dict[cell]) == 2:
                return self._function_dict[cell][1]
            else:
                return None
        else:
            return None
