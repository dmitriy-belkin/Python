from import_data_user import *
from printing_output import *


def search_data_user(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None