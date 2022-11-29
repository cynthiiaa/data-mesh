import csv
import sys
import fire

DATA_CATALOG_LOC = "data_catalog.csv"

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

    data_product_row = [name, locate_csv, attributes["Created_By"],
                        attributes["Department"], attributes["Schema"], attributes["Functionality"]]
    add_rows("", DATA_CATALOG_LOC, data_product_row)


if __name__ == "__main__":
    fire.Fire(register_data_product)
