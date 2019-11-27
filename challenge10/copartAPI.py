import requests
import json

class CopartAPI:
    def check(self):
        url = "https://www.copart.com/public/lots/search"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        return requests.get(url, headers=headers)
    def search(self, item):
        url = "https://www.copart.com/public/lots/search"
        headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
        query = {"query": item}
        response = requests.post(url, headers=headers, data=query)
        if response.status_code != 200:
            raise ConnectionError()
        jsonObject = json.loads(response.text)
        return jsonObject
