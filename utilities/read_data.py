import csv


def getCSVData(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # crete a CSV Reader from CSV file
    reader = csv.reader(data_file)
    #skip the headers
    next(reader)
    #add rows to the reader
    for row in reader:
        rows.append(row)
    return rows