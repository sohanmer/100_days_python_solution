import requests
import datetime as dt

TOKEN = "secret"
USERNAME = "username"

user_parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(
    url="https://pixe.la/v1/users",
    json=user_parameters
)
response.raise_for_status()

graph_parameters = {
    "id": "reading1",
    "name": "Reading Graph",
    "unit": "Hour",
    "type": "float",
    "color": "shibafu",
    "timezone": "Asia/Calcutta"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(
    url=f"https://pixe.la/v1/users/{USERNAME}/graphs",
    json=graph_parameters,
    headers=headers
)
response.raise_for_status()

graph_data = {
    "date": dt.datetime.now().strftime("%Y%m%d"),
    "quantity": input("How many hours did you read today? ")
}

response = requests.post(
    url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_parameters['id']}",
    json=graph_data,
    headers=headers
 )
response.raise_for_status()

graph_data_new = {
    "quantity": "3"
}

response = requests.put(
    url=f"https://pixe.la/v1/users/{USERNAME}/graphs/{graph_parameters['id']}/{graph_data['date']}",
    json=graph_data_new,
    headers=headers
)
response.raise_for_status()
