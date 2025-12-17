from unittest import TestCase, mock
from unittest.mock import Mock

import requests


def fetch_data():
    response = requests.get("https://api.example.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None

class TestFetchData(TestCase):

    @mock.patch("basic.testing.unittests_api.requests.get")
    def test_fetch_data_successful(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"key": "value"}

        mock_get.return_value = mock_response

        response = fetch_data()

        mock_get.assert_called_once_with("https://api.example.com/data")
        self.assertEqual(response["key"], "value")

    @mock.patch("basic.testing.unittests_api.requests.get")
    def test_fetch_data_unsuccessful(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        response = fetch_data()

        mock_get.assert_called_once()
        self.assertIsNone(response)
