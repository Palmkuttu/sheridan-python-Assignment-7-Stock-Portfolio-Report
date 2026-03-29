from collections import OrderedDict
import csv

def read_portfolio(filename):
    data = []

    with open(filename, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            item = OrderedDict()
            item["symbol"] = row["symbol"]
            item["units"] = row["units"]
            item["cost"] = row["cost"]

            data.append(item)

    return data
