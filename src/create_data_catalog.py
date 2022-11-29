import main

# creating empty data catalog
headers = ["Name", "Location", "Created_By", "ID",
           "Department", "Creation_Date", "Functionality", "Schema"]
folder = ""
filename = "data_catalog.csv"
main.write_csv_header(headers, folder, filename)

# inserting a data product into the data catalog
row = ["Machine Learning Data 4", "data/document1.csv", "Team Data Discoverers", "28",
       "SF Analytics", "04-23-2022", {"data_created": "01-01-1999", "attribute1": True, "attribute2": 500}, "Sentiment Analysis"]
main.add_rows(folder, filename, row)
