import requests
from flask import jsonify

def get_data():
    url = ('https://api.weatherapi.com'
           '/v1/history.json?q=45.267136%2C19.833549'
           '&dt=2024-04-21&end_dt=2024-04-21'
           '&key=c6031ec8223d4e4cb78224104241702')
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return f"Error: {response.status_code}", response.status_code