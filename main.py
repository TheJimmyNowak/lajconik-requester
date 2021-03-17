import sys
import time
import utils
from template_requests import TemplatePost


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

stop_time = time.time() - start

runner.save_stats()
print("Time elapsed: {} seconds".format(stop_time))
