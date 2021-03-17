import csv
import os
import json


class _TemplateRequest:
    def __init__(self, request_count, template_dir):
        self._template_dir = template_dir
        self._request_count = request_count
        self._stats = []
        self._url = str()
        self._template_data = []

    def send_request(self):
        pass

    def save_stats(self):
        with open('stats.csv', mode='w') as csv_file:
            stats_writer = csv.writer(csv_file, delimiter=',')
            stats_writer.writerows(self._stats)

    def read_template(self):
        data_path = os.path.join(self._template_dir, 'data')

        with open(data_path, "r") as data_file:
            self._url = data_file.readline()

        json_path = os.path.join(self._template_dir, 'template.json')

        with open(json_path, "r") as template_json:
            self._template_data = json.load(template_json)

    def make_random_data(self):
        pass


class TemplatePost(_TemplateRequest):
    def send_request(self):
        self.read_template()
        self.make_random_data()
