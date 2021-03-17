import sys
import time

from template_requests import *

requests_count = int(sys.argv[1])
url = sys.argv[2]
method = sys.argv[3]
global runner

start = time.time()

if method == "GET":
    utils.get_request(requests_count, url)
elif method == "POST":
    utils.post_request(requests_count, url)
elif method == "TEMPLATE-POST":
    runner = TemplatePost(requests_count, url)
    runner.send_request()
elif method == "TEMPLATE-GET":
    runner = TemplateGet(requests_count, url)
    runner.send_request()
elif method == "TEMPLATE-PUT":
    runner = TemplatePut(requests_count, url)
    runner.send_request()
elif method == "TEMPLATE-DELETE":
    runner = TemplateDelete(requests_count, url)
    runner.send_request()
elif method == "TEMPLATE-PATCH":
    runner = TemplatePatch(requests_count, url)
    runner.send_request()


stop_time = time.time() - start

runner.save_stats()
print("Time elapsed: {} seconds".format(stop_time))
