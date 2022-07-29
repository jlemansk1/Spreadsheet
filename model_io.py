import json


def write_to_json(file_handle, dict):
    json.dump(dict, file_handle)


def read_from_json(file_handle):
    dict = json.load(file_handle)
    return dict
