import pytest
import requests
from endpoints.products_endpoint import ProductsEndpoint


@pytest.fixture
def create_session():
    session = requests.session()
    yield session


@pytest.fixture
def api_endpoint(create_session):
    yield ProductsEndpoint(create_session)

