from string import ascii_lowercase
import itertools


def str_generator():
    for size in itertools.count(1):
        for x in itertools.product(ascii_lowercase, repeat=size):
            yield "".join(x)


def generate_dict(number_of_columns):
    dict = {}
    i = 0
    for column_name in itertools.islice(str_generator(), number_of_columns):
        column_name = column_name[0].upper() + column_name[1:]
        dict[i] = column_name
        i += 1
    return dict
