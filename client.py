import requests
import time
import json

class Client:
    def __init__(self):
        self.url = "http://api.facebeer.net:8000/append"

    def add_row(self, name, bac):
        current_time = time.localtime()
        timestamp = time.strftime("%m/%d/%y %H:%M", current_time)
        data = {"name": name, "bac": bac, "timestamp": timestamp}
        response = requests.post(self.url, data)
        response = json.loads(response.text)
        return response["code"]

# response = requests.post(url, data=data)
# print(response.text)
if __name__ == "__main__":
    client = Client()
    print(client.add_row("Max", .6))