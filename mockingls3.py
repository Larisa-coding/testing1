import requests
from unittest import TestCase
from unittest.mock import patch

THE_CAT_API_KEY = "live_bAKnLNBjOZbvtX4v33H41Ss1DzTgTOEieoOiizdMoKAkJtLZ9vNYueZBfgVeXCJB"
API_URL = "https://api.thecatapi.com/v1/images/search"


def get_random_cat_image():
    headers = {"x-api-key": THE_CAT_API_KEY}
    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list) and "url" in data[0]:
            return data[0]["url"]
    return None


class TestCatAPI(TestCase):

    @patch("requests.get")
    def test_successful_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = [{"url": "https://cdn2.thecatapi.com/images/abc.jpg"}]

        result = get_random_cat_image()
        self.assertEqual(result, "https://cdn2.thecatapi.com/images/abc.jpg")

    @patch("requests.get")
    def test_unsuccessful_request(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.json.return_value = []

        result = get_random_cat_image()
        self.assertIsNone(result)


if __name__ == "__main__":
    import unittest

    unittest.main()
