import csv
from judy_objects import Item

ITEM_NAME_FIELD_KEY = 'item_name'
PROBABILITY_FIELD_KEY = 'probability'
EMPTY_FIELD_KEY = ''

def _read_csv_to_dictionary_list(file_name):
    """
    Reads a CSV file for a catalog into a long format Python dictionary.
    The first line is assumed to be the header line, and must contain the field 'item_name'.
    """
    catalog_list = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            catalog_list.append(item)
    return catalog_list

def _sanitize_item(item_dict):
    #del item_dict[EMPTY_FIELD_KEY]
    del item_dict[ITEM_NAME_FIELD_KEY]
    del item_dict[PROBABILITY_FIELD_KEY]
    return item_dict
    
def _get_schema(item):
    i = 0
    schema = {}

    for field in item:
        schema[field] = i
        i += 1
    return schema

def get_catalog(file_name):
    catalog_list = _read_csv_to_dictionary_list(file_name)
    schema = {}
    catalog = []

    for item in catalog_list:
        name = item[ITEM_NAME_FIELD_KEY]
        p = item[PROBABILITY_FIELD_KEY]
        bitmap  = ''

        sanitized_item = _sanitize_item(item)
        schema = _get_schema(sanitized_item)

        for key in schema:
            bitmap += sanitized_item[key]

        catalog.append(Item(name, p, bitmap))
    catalog.sort(key = lambda x:x.probability)
    return schema, catalog
