import requests
from flask import jsonify
from SimulatorSrv.Models.ResponseStatus import ResponseStatus
def get_data():
    url = ('https://api.weatherapi.com'
           '/v1/history.json?q=45.267136%2C19.833549'
           '&dt=2024-07-8&end_dt=2024-07-08'
           '&key={api_key}')
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        ret = ResponseStatus(status=200, value=data, message="Success")
        return ret
    else:
        ret = ResponseStatus(status=400,value="", message=f"Error: {response.status_code}")
        return ret
