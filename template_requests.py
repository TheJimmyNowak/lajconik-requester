import csv
import json
import os
import random

import requests

import utils


class _Request:
    def __init__(self, request_count: int, template_dir: str):
        self._template_dir = template_dir
        self._request_count = request_count
        self._stats = []
        self._url = str()
        self._template_data = []

    def send_request(self) -> None:
        print("[ERROR] send_request() wasn't implemented!")

    def save_stats(self) -> None:
        with open('stats.csv', mode='w') as csv_file:
            stats_writer = csv.writer(csv_file, delimiter=',')
            stats_writer.writerows(self._stats)

    def read_template(self) -> None:
        data_path = os.path.join(self._template_dir, 'data.txt')

        with open(data_path, "r") as data_file:
            self._url = data_file.readline()

        json_path = os.path.join(self._template_dir, 'template.json')

        try:
            with open(json_path, "r") as template_json:
                self._template_data = json.load(template_json)
        except:
            print("[Error] template.json doesn't exist")

    def make_random_data(self) -> dict:
        data = self._template_data.copy()

        for i in data:
            type_to_gen = str()
            min_length = 0
            max_length = 255
            quantity = 0
            key = ""
            value_type = ""

            try:
                if len(str(data[i]).split()) == 2:
                    type_to_gen = str(data[i]).split()[0]
                    max_length = int(str(data[i]).split()[1])
                    min_length = 0
                elif len(str(data[i]).split()) == 3:
                    type_to_gen = str(data[i]).split()[0]
                    min_length = int(str(data[i]).split()[1])
                    max_length = int(str(data[i]).split()[2])
                elif len(str(data[i]).split()) == 4:
                    type_to_gen = str(data[i]).split()[0]
                    quantity = int(str(data[i]).split()[1])
                    min_length = int(str(data[i]).split()[2])
                    max_length = int(str(data[i]).split()[3])
                elif len(str(data[i]).split()) == 6:
                    type_to_gen = str(data[i]).split()[0]
                    key = str(data[i]).split()[1]
                    quantity = int(str(data[i]).split()[2])
                    value_type = str(data[i]).split()[3]
                    min_length = int(str(data[i]).split()[4])
                    max_length = int(str(data[i]).split()[5])
                else:
                    type_to_gen = "NaN"

            except IndexError:
                print(data[i])
            except ValueError:
                print(data[i])

            if type_to_gen == "int":
                data[i] = random.randint(min_length, max_length)
            elif type_to_gen == "str":
                data[i] = utils.get_random_str(max_length=max_length)
            elif type_to_gen == "list":
                data[i] = [utils.get_random_str(min_length=min_length, max_length=max_length) for i in range(quantity)]
            elif type_to_gen == "dictlist":
                if value_type == "str":
                    data[i] = [{key: utils.get_random_str(min_length=min_length, max_length=max_length)} for i in
                               range(quantity)]
                elif value_type == "int":
                    data[i] = [{key: random.randint(min_length, max_length)} for i in range(quantity)]

        return data


class Post(_Request):
    def send_request(self):
        self.read_template()
        data = [self.make_random_data() for i in range(self._request_count)]

        for i in range(self._request_count):
            res = requests.post(self._url, data=data[i])
            self._stats.append([res.elapsed.total_seconds()])


class Get(_Request):
    def send_request(self) -> None:
        self.read_template()
        for i in range(self._request_count):
            res = requests.get(self._url)
            self._stats.append([res.elapsed.total_seconds()])


class Put(_Request):
    def send_request(self):
        self.read_template()
        data = [self.make_random_data() for i in range(self._request_count)]

        for i in range(self._request_count):
            res = requests.put(self._url, data=data[i])
            self._stats.append([res.elapsed.total_seconds()])


class Delete(_Request):
    def send_request(self):
        self.read_template()

        for i in range(self._request_count):
            res = requests.delete(self._url)
            self._stats.append([res.elapsed.total_seconds()])


class Patch(_Request):
    def send_request(self):
        self.read_template()
        data = [self.make_random_data() for i in range(self._request_count)]

        for i in range(self._request_count):
            res = requests.patch(self._url, data=data[i])
            self._stats.append([res.elapsed.total_seconds()])
