from pathlib import Path
import json


def read_data(file_name, field):
    #get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name


    if field not in {"unordered_numbers", "sequential.json", "dna_sequence"}:
        return None
    else:
        with open(file_path, "r") as fil:
            dat = json.load(fil)
        return dat[field]


    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path

def linear_search(sequence, number):
    count = 0
    pozicia = []

    for index, numb in enumerate(sequence):
        if number == numb:
            count += 1
            pozicia.append(index)
    dict = {"position": pozicia, "count":count}
    return dict





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    dict = linear_search(sequential_data, number = 5)
    print(dict)


if __name__ == "__main__":
    main()
