from unittest import TestCase

from template_requests import *
from template_requests import _Request


class TestRequest(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRequest, self).__init__(*args, **kwargs)
        self.obj = _Request(2, "tests/templates/test-template")

    def test_make_random_data(self):
        self.obj.read_template()
        data = self.obj.make_random_data()

        # Test Int generation
        self.assertGreaterEqual(data['testint'], 10, "Int generation doesn't work")
        self.assertLessEqual(data['testint'], 200, "Int generation doesn't work")

        self.assertGreaterEqual(data['testint2'], 0, "Int generation doesn't work")
        self.assertLessEqual(data['testint'], 220, "Int generation doesn't work")

        # Test string generation
        self.assertGreaterEqual(len(data['teststr']), 123, "Str generation doesn't work")
        self.assertLessEqual(len(data['teststr']), 200, "Str generation doesn't work")

        self.assertGreaterEqual(len(data['teststr2']), 0, "Str generation doesn't work")
        self.assertLessEqual(len(data['teststr2']), 12, "Str generation doesn't work")

        # Test list generation
        self.assertEqual(len(data["testlist"]), 2, "List generation doesn't work")
        self.assertGreaterEqual(len(data['testlist'][1]), 20, "List generation doesn't work")
        self.assertLessEqual(len(data['testlist'][1]), 23, "List generation doesn't work")

        # Test dictlist generation
        self.assertEqual(len(data["testdictlist"]), 10, "Dictlist generation doesn't work")
        self.assertGreaterEqual(data['testdictlist'][3]['name'], 3, "Dictlist generation doesn't work")
        self.assertLessEqual(data['testdictlist'][3]['name'], 20, "Dictlist generation doesn't work")


class TestPost(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPost, self).__init__(*args, **kwargs)
        self.obj = Post(1, 'tests/templates/test-template')

    def test_send_request(self):
        stats_path = utils.get_random_str(0, 20) + ".csv"

        self.obj.send_request()
        self.obj.save_stats(stats_path)

        with open(stats_path, 'r') as stats:
            reader = csv.reader(stats, delimiter=",")
            next(reader)
            res_time, status_code = next(reader)

            self.assertTrue(type(res_time) is not None)
            self.assertEqual(int(status_code), 404)

        os.remove(stats_path)


class TestGet(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestGet, self).__init__(*args, **kwargs)
        self.obj = Get(1, 'tests/templates/test-template')

    def test_send_request(self):
        stats_path = utils.get_random_str(0, 20) + ".csv"

        self.obj.send_request()
        self.obj.save_stats(stats_path)

        with open(stats_path, 'r') as stats:
            reader = csv.reader(stats, delimiter=",")
            next(reader)
            res_time, status_code = next(reader)

            self.assertTrue(type(res_time) is not None)
            self.assertEqual(int(status_code), 404)

        os.remove(stats_path)


class TestPut(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPut, self).__init__(*args, **kwargs)
        self.obj = Put(1, 'tests/templates/test-template')

    def test_send_request(self):
        stats_path = utils.get_random_str(0, 20) + ".csv"

        self.obj.send_request()
        self.obj.save_stats(stats_path)

        with open(stats_path, 'r') as stats:
            reader = csv.reader(stats, delimiter=",")
            next(reader)
            res_time, status_code = next(reader)

            self.assertTrue(type(res_time) is not None)
            self.assertEqual(int(status_code), 404)

        os.remove(stats_path)


class TestDelete(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestDelete, self).__init__(*args, **kwargs)
        self.obj = Delete(1, 'tests/templates/test-template')

    def test_send_request(self):
        stats_path = utils.get_random_str(0, 20) + ".csv"

        self.obj.send_request()
        self.obj.save_stats(stats_path)

        with open(stats_path, 'r') as stats:
            reader = csv.reader(stats, delimiter=",")
            next(reader)
            res_time, status_code = next(reader)

            self.assertTrue(type(res_time) is not None)
            self.assertEqual(int(status_code), 404)

        os.remove(stats_path)


class TestPatch(TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPatch, self).__init__(*args, **kwargs)
        self.obj = Patch(1, 'tests/templates/test-template')

    def test_send_request(self):
        stats_path = utils.get_random_str(0, 20) + ".csv"

        self.obj.send_request()
        self.obj.save_stats(stats_path)

        with open(stats_path, 'r') as stats:
            reader = csv.reader(stats, delimiter=",")
            next(reader)
            res_time, status_code = next(reader)

            self.assertTrue(type(res_time) is not None)
            self.assertEqual(int(status_code), 404)

        os.remove(stats_path)
