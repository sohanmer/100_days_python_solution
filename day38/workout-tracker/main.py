import requests
import datetime as dt

APP_ID = "<app_id>"
API_KEY = "<api_key>"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercise you did: ")
}

response = requests.post(url=NUTRITIONIX_URL, json=parameters, headers=headers)
response.raise_for_status()
exercises = response.json()['exercises']

SHEETY_URL = "https://api.sheety.co/d7c610269b62e4d1afa915d55757abfb/myWorkouts/workouts"
SHEETY_TOKEN = "<sheety_token>"

headers = {
    "Authorization": "Bearer <auth_token>"
}

workouts = {}
for exercise in exercises:
    workouts["workout"] = {
        "date": dt.datetime.today().strftime('%Y-%m-%d'),
        "time": dt.datetime.today().strftime('%H:%M:%S'),
        "exercise": exercise['user_input'],
        "duration": exercise['duration_min'],
        "calories": exercise['nf_calories']
    }
    response = requests.post(SHEETY_URL, json=workouts, headers=headers)
    response.raise_for_status()
    print("Exercise added to your sheet.")
    workouts = {}
