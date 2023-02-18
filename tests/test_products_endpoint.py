import pytest

def test_status_up(api_endpoint):
    api_endpoint.check_status_response()


def test_create_cart(api_endpoint):
    api_endpoint.check_post_cart_created()


def test_create_item(api_endpoint):
    api_endpoint.check_created_item()

def test_delete_item(api_endpoint):
    api_endpoint.post_add_item_to_cart()




