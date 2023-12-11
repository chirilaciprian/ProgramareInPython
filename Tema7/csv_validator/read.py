import csv
def read_data(path):
    file = open(path)
    csvreader = csv.reader(file)
    header = next(csvreader)
    rows = []
    for row in csvreader:
        rows.append(row)
    return header, rows    