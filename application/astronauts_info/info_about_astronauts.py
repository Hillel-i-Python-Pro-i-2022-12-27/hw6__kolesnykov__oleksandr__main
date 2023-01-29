import requests


astronauts_api = "http://api.open-notify.org/astros.json"


def make_json_request():

    response = requests.get(astronauts_api)

    if response.status_code == 200:
        response = response.json()
        return response

    return f"Что-то пошло не так, код проблемы: {response.status_code}"


def list_of_astronauts():

    response = make_json_request()

    if isinstance(response, dict):
        list_of_names = []
        for astronaut in response["people"]:
            list_of_names.append(astronaut["name"])

        return list_of_names
    return response


def get_count_of_astronauts():

    response = make_json_request()

    if isinstance(response, dict):
        count_of_astronauts = response["number"]

        return count_of_astronauts
    return response


def get_info():
    return get_count_of_astronauts(), list_of_astronauts()
