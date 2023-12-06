import requests
import unittest

class ApiRequestError(Exception):
    pass

class ApiRequest:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def make_api_request(self, method, url, data=None):
        try:
            URL = f'{self.base_url}/{url}'
            response = requests.request(method=method, url=URL, json=data)
            response.raise_for_status()
            return response.json() if response.text else None # JSON Format Response
        except requests.exceptions.InvalidURL as invalid_url:
            raise ApiRequestError(f'Request Failed: {invalid_url}')
        except requests.exceptions.HTTPError as http_error:
            raise ApiRequestError(f'Request Failed: {http_error}')
        except requests.exceptions.ConnectionError as connection_error:
            raise ApiRequestError(f'Request Failed: {connection_error}')
        except requests.exceptions.TooManyRedirects as too_many_redirects_error:
            raise ApiRequestError(f'Request Failed: {too_many_redirects_error}')
        except requests.exceptions.Timeout as timeout_error:
            raise ApiRequestError(f'Request Failed: {timeout_error}')
        except requests.exceptions.ConnectTimeout as connection_timeout_error:
            raise ApiRequestError(f'Request Failed: {connection_timeout_error}')
        except Exception as ex:
            raise ApiRequestError(f'unknown exception occured as {ex}')
        

class ApiRequestTest(unittest.TestCase):
    def setUp(self):
        self.api = ApiRequest("https://jsonplaceholder.typicode.com")
        
    def test_get_api_request(self):
        method = 'GET'
        response = self.api.make_api_request(method=method, url='posts')
        self.assertIsNotNone(response)

    def test_get_api_request_exception(self):
        method = 'GET'
        with self.assertRaises(ApiRequestError): 
            response = self.api.make_api_request(method=method, url='nonexixstenturl')

    def test_delete_api_request(self):
        method = 'DELETE'
        response = self.api.make_api_request(method=method, url='posts/1')
        self.assertEqual(response, {})

    def test_post_api(self):
        method = 'POST'
        data = {'userId': 1, 'title': 'Happy birthday', 'body': 'Happy birthday! let\'s dance'}
        response = self.api.make_api_request(method=method, url='posts', data=data)
        self.assertIsNotNone(response)
        

if __name__ == '__main__':
    unittest.main()