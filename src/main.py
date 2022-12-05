import csv
import sys
import pandas as pd
import fire

DATA_CATALOG_LOC = "./data_catalog.csv"
DATA_PRODUCTS = []

#------------------- Helper Functions for File Parsing -------------------#


def parse_config(config):
    with open(config, "r") as f:
        lines = f.readlines()
    return lines


def write_csv_header(headers, folder, filename):
    with open(folder + filename, "w", newline="") as f:
        document = csv.writer(f)
        document.writerow(headers)


def add_rows(folder, filename, row):
    with open(folder+filename, "a", newline="") as f:
        document = csv.writer(f)
        document.writerow(row)


#------------------- Data Product Registration Functions -------------------#
def register_csv_port(name):
    headers = ["ID", "Timestamp"]
    folder = "data/"
    filename = f"{name}.csv"
    write_csv_header(headers, folder, filename)
    return folder + filename


def register_data_product(name="empty_data_product", attributes={}):
    print(f"Registering {name} CSV port...")
    locate_csv = register_csv_port(name)

    data_product_row = [name, locate_csv, attributes["Created_By"], attributes["ID"],
                        attributes["Department"], attributes["Creation_Date"], attributes["Schema"], attributes["Functionality"]]
    add_rows("", DATA_CATALOG_LOC, data_product_row)


#------------------- Access Data Products  -------------------#
def list_data_products():
    with open(DATA_CATALOG_LOC, 'r') as f:
        next(f)
        lines = f.readlines()
        print(f"There are {len(lines)} Data Products:\n")
        for line in lines:
            print(line)


def get_data_product_location(data_product_name):
    with open(DATA_CATALOG_LOC, 'r') as f:
        next(f)
        csv_file = csv.reader(f)
        data_products = {}
        locations = {}

        for entry in csv_file:
            locations["location_csv"] = entry[1]
            data_products[entry[0]] = locations

    return data_products[data_product_name]


def load_data(data_product_name):
    locs = get_data_product_location(data_product_name)
    return pd.read_csv(locs["location_csv"], header=0)


if __name__ == "__main__":
    fire.Fire(load_data)
