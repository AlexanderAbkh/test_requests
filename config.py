import os
import json



BASE_API = "https://simple-grocery-store-api.glitch.me"
# *************** GET ****************
STATUS_ENDPOINT = os.path.join(str(BASE_API) + "/status")
PRODUCTS_ENDPOINT = os.path.join(str(BASE_API) + "/products")
# **** with query param
PRODUCTS_ENDPOINT_PATH_PARAM_PRODUCT_ID = os.path.join(str(PRODUCTS_ENDPOINT) + "/{}")
# ************ POST *******************
CART_ENDPOINT = os.path.join(str(BASE_API) + "/carts")
# with path param
CART_ITEMS_ENDPOINT = os.path.join(str(BASE_API) + "/carts/{}/items")
#test_data
BASE_PATH = os.path.dirname(os.path.realpath(__file__))

DELETE_ITEM_FROM_ORDER = os.path.join(str(BASE_API) + "/carts/{}/items/{}")


data_path = os.path.join(BASE_PATH, 'test_data', 'data.json')

with open(data_path, 'r') as products_data:
    """
    Тут константам присваивается необходимое значение, конструкция нужна для того чтобы спарсить значения из модуля
    data.json в котором словарь находится в списке
    """
    products = json.load(products_data)
status_value = products[0]
STATUS_RESPONSE = status_value["status_response"]
cart_value = products[1]
CART_CREATED = cart_value["status_cart_created"]
