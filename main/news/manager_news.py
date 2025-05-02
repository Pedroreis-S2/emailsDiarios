import os
from __init__ import *

class ManagerNews:
    topic: str = ""
    controller = None

    def __init__(self, topic: str = "") -> property:
        if topic:
            self.topic = "&q=" + topic
        self.update_url()
        self.get_news()
        pass

    def get_token(self) -> str:
        return os.environ.get("APIKEYNEWS", "")
    
    def update_url(self) -> any:
        token = self.get_token()
        self.controller = NewsController(api_key=token)
        if self.topic:
            self.controller.base_url += self.topic
        return
    
    def get_news(self):
        news: bool = self.controller.get_news()
        if not news:
            self.last_error = self.controller.last_error
            return False
        data = self.controller.data
        print("controler data: ", self.controller.data)
        return True
        
