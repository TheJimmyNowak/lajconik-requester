from functools import reduce

import requests
import string
import random

response_times = []


def get_request(requests_count: int, url: str) -> None:
    for i in range(requests_count):
        res = requests.get(url)
        response_times.append(res.elapsed.total_seconds())


def post_request(requests_count: int, url: str) -> None:
    data = [get_random_json() for i in range(requests_count)]

    for i in range(requests_count):
        res = requests.post(url, data=data[i])
        response_times.append(res.elapsed.total_seconds())


def get_random_str(length: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))


def get_random_json():
    return {
        "title": get_random_str(255),
        "description": get_random_str(255),
        "gameMaster": {
            "id": 2
        },
        "maxPlayerNumber": str(random.randint(1, 8)),
        "minAge": "15",
        "minSkill": get_random_str(255),
        "availableTimeslots": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ],
        "rpgSystem": get_random_str(255),
        "streamable": True,
        "sidenotes": get_random_str(255),
        "publiclyAvailable": True
    }


def show_stats() -> None:
    average = reduce(lambda a, b: a + b, response_times) / len(response_times)
    print("Average response time is: {}" .format(average))
