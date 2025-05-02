import json
import requests
import os

class NewsController:
    base_url = None
    data = None

    def __init__(self, api_key: str) -> property:
        self.base_url = "https://newsdata.io/api/1/news?apikey={}&country=br".format(api_key)
    
    def get_news(self) -> bool:
        response = requests.get(self.base_url)
        if response.status_code != 200:
            self.last_error = "Erro ao buscar as notícias " + str(response.status_code)
            print(self.last_error)
            return False 

        data = response.json()
        self.data = data.get("results")
        # with open("news.json", "w") as file:
        #     data = json.dumps(data, indent=4)
        #     file.write(str(data))

        return True