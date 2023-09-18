import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        URL = self.url
        
        response = requests.get(URL)
        return response.content

    def load_json(self):
        data = []
        x = json.loads(self.get_response_body())
        
        for y in x:
            data.append(y)
            
        return data    
        