""" Test endpoints from Flask CRUD API """

import requests
import pytest
from requests.models import Response


class TestEndpoints:

    @pytest.fixture
    def setup(self) -> None:
        self.id = 1  # Used for other tests

    """ Test the create endpoint """
    def test_01_create_endpoint(self, setup) -> None:
        """ Connect to the create endpoint """
        url: str = "http://127.0.0.1:5000/create"
        data: dict = {'name': "Austin Uwate",
                      'id': 1,
                      "description": "A CS student learning every day."}
        response: Response = requests.post(url=url, json=data)

        test_data: dict = response.json()

        assert test_data, "Invalid return"
        assert (
            'code' in test_data and
            'response' in test_data
        ), test_data
        assert (
                200 == test_data['code'] and
                'success' == test_data['response']
        ), test_data

    def test_02_read_endpoint(self, setup) -> None:
        """ Connect to the read endpoint """
        url: str = "http://127.0.0.1:5000/read"
        response: Response = requests.get(url=url)

        test_data: dict = response.json()

        assert test_data, "Invalid return"
        assert (
            'code' in test_data and
            'response' in test_data and
            len(test_data['response']) == 1
        ), test_data
        assert (
            'name' in test_data['response'][0] and
            'Austin Uwate' == test_data['response'][0]['name'] and
            'attributes' in test_data['response'][0]
        ), test_data['response']
        assert (
            'id' in test_data['response'][0]['attributes'] and
            'description' in test_data['response'][0]['attributes']
        ), test_data['response'][0]['attributes']
        assert (
                1 == test_data['response'][0]['attributes']['id'] and
                'A CS student learning every day.' ==
                test_data['response'][0]['attributes']['description']
        ), test_data['response'][0]['attributes']

    def test_03_update_endpoint(self, setup) -> None:
        """ Connect to the update endpoint """
        url: str = "http://127.0.0.1:5000/update"
        data: dict = {'name': "Tyler", "description": "My brother", 'id': self.id}
        response: Response = requests.put(url=url, json=data)

        test_data: dict = response.json()

        assert test_data, "Invalid return"
        assert (
                'code' in test_data and
                'response' in test_data
        ), test_data
        assert (
                200 == test_data['code'] and
                'success' == test_data['response']
        ), test_data

    def test_04_delete_endpoint(self, setup) -> None:
        """ Connect to the delete endpoint """
        url: str = "http://127.0.0.1:5000/delete"
        data: dict = {'id': self.id}
        response: Response = requests.delete(url=url, json=data)

        test_data: dict = response.json()

        assert test_data, "Invalid return"
        assert (
                'code' in test_data and
                'response' in test_data
        ), test_data
        assert (
                200 == test_data['code'] and
                'success' == test_data['response']
        ), test_data
