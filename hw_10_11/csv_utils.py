import csv


def read_file(some_file: str):
    with open(some_file) as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)


def adding_text(some_file: str):
    with open(some_file, 'a') as my_file:
        my_file.writelines(['coca-cola,', '2,', '100,', 'better with whiskey'])
        return my_file


def del_text(some_file: str):
    file = open(some_file).readlines()
    del_3_arg = file.pop(3)
    with open(some_file, 'w') as File:
        File.writelines(file)



