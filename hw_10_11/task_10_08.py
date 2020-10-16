import csv
from csv_utils import read_file, adding_text, del_text

fields = ['Name of product', 'price', 'number', 'comments']
rows = [
    ['Tea', 2.0, 40, 'Nice tea'],
    ['Coffee', 7.5, 23, 'Good coffee'],
    ['Sweets', 6.8, 32, 'very sweet'],
    ['Cookie', 3.3, 100, 'tasteless'],
]
filename = 'students_info.csv'
with open(filename, 'w') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(fields)
    csvwrite.writerows(rows)


# adding_text('students_info.csv')
# del_text('students_info.csv', 3)
# print(read_file('students_info.csv'))
