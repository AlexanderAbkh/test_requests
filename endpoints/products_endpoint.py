from base_api.base import BaseApi
from config import *


class ProductsEndpoint(BaseApi):

    def __init__(self, session):
        super().__init__(session)


    def get_status_up(self):

        return self.get_parsed_json(STATUS_ENDPOINT)


    def check_status_response(self):

        actual_response = self.get_status_up()
        expected_response = STATUS_RESPONSE
        self.assertion_equal(actual_response, expected_response)

    def post_cart(self):

        return self.post_parsed_json(CART_ENDPOINT)





    def check_post_cart_created(self):

        actual_response = self.post_cart()
        expected_response = CART_CREATED
        self.assertion_equal(actual_response, expected_response)

    def post_add_item_to_cart(self):

        payload = {"productId": "4643"}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        return self.post_parsed_json(CART_ITEMS_ENDPOINT.format('1235'), data=json.dumps(payload), headers=headers)

    def check_created_item(self):

        actual_response = self.post_add_item_to_cart()
        expected_response = 1
        self.assertion_equal(actual_response, expected_response)


    def delete_item_from_order(self):
        resp = self.delete_parsed_json(DELETE_ITEM_FROM_ORDER.format('123', '123'))
        print(resp)




