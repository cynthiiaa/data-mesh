import csv
import sys


"""
This function takes in a configuration file for a data product
"""


def parse_config(config):
    with open(config, "r") as f:
        lines = f.readlines()
    return lines


"""
This function takes in a string for the product name and a 
list of values for the schema.

Example
name: movie
schema: [title, year_released, category, length, country, language]
"""


def register_data_product(name, schema):
    with open(f"data/{name}.csv", "w") as f:
        document = csv.writer(f)
        document.writerow(schema)


if __name__ == "__main__":
    file = sys.argv[1]
    config = parse_config(file)
    name = config[0].strip()
    schema = config[1].strip().split(",")

    register_data_product(name, schema)
