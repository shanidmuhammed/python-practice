# Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.

import tablib

def csv_to_excel(csv_file, excel_file):
    data = tablib.Dataset()

    with open(csv_file) as c:
        for line in c:
            data.append(line)
    with open(excel_file, 'wb') as e:
        e.write(data.xls)

csv_to_excel('data.csv', 'data.xls')