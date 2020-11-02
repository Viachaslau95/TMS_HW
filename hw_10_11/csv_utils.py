import csv


def read_file(some_file: str):
    rows = []
    with open(some_file) as file:
        fields = next(file)
        for row in file:
            rows.append(row)
    return fields, rows


def adding_text(some_file: str):
    with open(some_file, 'a') as my_file:
        my_file.writelines(['coca-cola,', 2.0 , 100, 'better with whiskey'])
        return my_file


def del_text(some_file: str, number_line: int):
    file = open(some_file).readlines()
    file.pop(number_line)
    with open(some_file, 'w') as File:
        File.writelines(file)


def sum_price(some_file: str, rows: list):
    s = 0
    for i in range(len(rows)):
        s += rows[i][1]
    print(s)


