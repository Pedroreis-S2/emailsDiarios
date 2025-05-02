import os
from __init__ import *

def execute():
    topic = os.environ.get("TOPIC", "tecnologia")
    manager = ManagerNews(topic=topic)
    pass