import csv
from csv_utils import read_file, adding_text, del_text

fields = ['Name of product', 'price', 'number', 'comments']
rows = [
    ['Tea', '3', '40', 'Nice tea'],
    ['Coffee', '7', '23', 'Good coffee'],
    ['Sweets', '5', '32', 'very sweet'],
    ['Cookie', '6', '24', 'tasteless'],
]
filename = 'students_info.csv'
with open(filename, 'w') as csvfile:
    csvwrite = csv.writer(csvfile)
    csvwrite.writerow(fields)
    csvwrite.writerows(rows)


# adding_text('students_info.csv')
# del_text('students_info.csv')
# read_file('students_info.csv')

