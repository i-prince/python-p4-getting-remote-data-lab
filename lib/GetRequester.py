import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send a GET request to the URL and return the response body
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        # Use get_response_body to get the response body
        response_body = self.get_response_body()

        # Convert the response body to a Python list or dictionary
        try:
            json_data = json.loads(response_body)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
