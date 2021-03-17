import csv
import json
import os
import random

import requests

import utils


class _TemplateRequest:
    def __init__(self, request_count: int, template_dir: str):
        self._template_dir = template_dir
        self._request_count = request_count
        self._stats = []
        self._url = str()
        self._template_data = []

    def send_request(self) -> None:
        pass

    def save_stats(self) -> None:
        with open('stats.csv', mode='w') as csv_file:
            stats_writer = csv.writer(csv_file, delimiter=',')
            stats_writer.writerows(self._stats)

    def read_template(self) -> None:
        data_path = os.path.join(self._template_dir, 'data.txt')

        with open(data_path, "r") as data_file:
            self._url = data_file.readline()

        json_path = os.path.join(self._template_dir, 'template.json')

        with open(json_path, "r") as template_json:
            self._template_data = json.load(template_json)

    # TODO: Dict handling
    def make_random_data(self) -> dict:
        data = self._template_data.copy()

        for i in data:
            try:
                type_to_gen = str(data[i]).split()[0]
                length = int(str(data[i]).split()[1])
            except IndexError:
                print("IndexError ")
            except ValueError:
                print("ValueError ")

            if type_to_gen == "int":
                data[i] = random.randint(0, length)
            if type_to_gen == "str":
                data[i] = utils.get_random_str(length)

        return data

    def save_stats(self) -> None:
        with open('stats.csv', mode='w') as csv_file:
            stats_writer = csv.writer(csv_file, delimiter=',')
            stats_writer.writerows(self._stats)


class TemplatePost(_TemplateRequest):
    def send_request(self):
        self.read_template()
        data = [self.make_random_data() for i in range(self._request_count)]

        for i in range(self._request_count):
            res = requests.post(self._url, data=data[i])
            self._stats.append([res.elapsed.total_seconds()])


