import main

#------------- Registering Data Products -------------#
data_products_attributes = {
    "Created_By": "Team Data Discoverers",
    "Functionality": "Sentiment Analysis 6",
    "Department": "SF Analytics",
    "Schema": '{"data_created": "01-01-1999", "attribute1": True, "attribute2": 500}'
}
main.register_data_product(name="DataProductTest1",
                           attributes=data_products_attributes)


data_products_attributes2 = {
    "Created_By": "Inner Insight",
    "Functionality": "EDA",
    "Department": "DC Analytics",
    "Schema": '{"data_created": "01-01-2012", "attribute1": False, "attribute2": 9001}'
}
main.register_data_product(name="DataProductTest2",
                           attributes=data_products_attributes2)