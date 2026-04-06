import csv
from collections import OrderedDict


def read_portfolio(filename):
    result = []

    with open(filename, 'r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            ordered = OrderedDict()
            ordered['symbol'] = row['symbol']
            ordered['units'] = row['units']
            ordered['cost'] = row['cost']
            result.append(ordered)

    return result


def save_portfolio(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # header
        writer.writerow(['symbol', 'units', 'cost'])

        # rows
        for item in data:
            writer.writerow([
                item['symbol'],
                item['units'],
                item['cost']
            ])
