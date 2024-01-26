import requests
import json
from bs4 import BeautifulSoup
from dataclasses import dataclass
from dotenv import load_dotenv
import os
load_dotenv()

google_api = os.getenv("GOOGLE_API")

@dataclass
class Item:
    Index: int
    Title: str
    Link: str
    Trailer: str

class MakingRequest:
    url = "https://google.serper.dev/search"
    headers = {
        'X-API-KEY': f'{google_api}',
        'Content-Type': 'application/json'
    }
    def __init__(self,param):
        self.param = param

    @property
    def payload(self):
        return json.dumps({"q": f"{self.param}",})

    def making_response(self):
        return requests.request("POST", self.url, headers=self.headers, data=self.payload)

    def making_json_data(self):
        return json.loads((self.making_response()).text)

class MakingJson:
    def start(self, value):
        self.param = value
        self.data = self.returning_json_req()

        print(json.dumps(self.making_body(), indent=4))
    def returning_json_req(self):
        return MakingRequest(self.param).making_json_data()

    @property
    def knowlage_graph(self):
        knowledge_graph = self.data.get('knowledgeGraph', {})
        title = knowledge_graph.get('title', 'N/A')
        description = knowledge_graph.get('description', 'N/A')
        attributes = knowledge_graph.get('attributes', 'N/A')
        knowledge_graph = {
            'title' : title,
            'description' : description,
            'attributes' : attributes,
        }
        return knowledge_graph

    @property
    def organic_results(self):
        organic_results = self.data['organic']
        ret_result = list()
        if organic_results:
            for i, result in enumerate(organic_results):
                ret_result.append(Item(i + 1, result['title'], result['link'], result['snippet']))
        else:
            print("No organic results found.")

        return ret_result

    def making_body(self):
        head = self.knowlage_graph
        body = self.organic_results

        json_body = {
            "Head": head,
            "Body": [item.__dict__ for item in body]
        }
        return json_body


if __name__ == "__main__":
    json_obj = MakingJson()
    json_obj.start(value="Tank t-90")