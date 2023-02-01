"""
Reads and writes JSON files to specified file paths.
"""
import json
import os.path


def write(data, path):
    """
    Writes specified data to a specified path in the JSON format.

    :param data: to be written to a file.
    :param path: string path to the file "./data/example.json"
    :return: FileNotFoundError.
    """
    # Check if file exists.
    if os.path.isfile(path):
        # Open the file and write data.
        with open(path, 'w') as json_file:
            json.dump(data, json_file)
    else:
        return FileNotFoundError


def read(path):
    """
    Reads from specified path and returns the data.

    :param path: string path to the file "./data/example.json"
    :return: the data in the file or FileNotFoundError.
    """
    # Check if file exists.
    if os.path.isfile(path):
        # Open the file and read data.
        with open(path, 'r') as json_file:
            return json.load(json_file)
    else:
        return FileNotFoundError
