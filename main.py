"""
PIXELA API
"""


import requests
from datetime import datetime

TOKEN = "iodfgaisopjgiodsfgj"
USERNAME = "olegdavimuka"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Money Graph",
    "unit": "UAH",
    "type": "int",
    "color": "ajisai"
}

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1400",
}

# Create a User
# response = requests.post(url=pixela_endpoint, json=user_params)

# Create a Graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

# Create a Pixel
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
