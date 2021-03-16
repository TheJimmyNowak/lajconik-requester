from functools import reduce

import requests
import string
import random
import csv

stats = []


def get_request(requests_count: int, url: str) -> None:
    for i in range(requests_count):
        res = requests.get(url)
        stats.append([res.elapsed.total_seconds()])


def post_request(requests_count: int, url: str) -> None:
    data = [get_random_json() for i in range(requests_count)]

    for i in range(requests_count):
        res = requests.post(url, data=data[i])
        stats.append([res.elapsed.total_seconds()])


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

"""
def show_stats() -> None:
    average = reduce(lambda a, b: a + b, stats) / len(stats)
    print("Average response time is: {}" .format(average))
"""


def save_stats() -> None:
    print(stats)
    with open('stats.csv', mode='w') as csv_file:
        stats_writer = csv.writer(csv_file, delimiter=',')
        stats_writer.writerows(stats)