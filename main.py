import sys
import time

import template_requests

requests_count = int(sys.argv[1])
template_dir = sys.argv[2]
method = str(sys.argv[3]).upper()
global runner

start = time.time()

if method == "POST":
    runner = template_requests.Post(requests_count, template_dir)
    runner.send_request()
elif method == "GET":
    runner = template_requests.Get(requests_count, template_dir)
    runner.send_request()
elif method == "PUT":
    runner = template_requests.Put(requests_count, template_dir)
    runner.send_request()
elif method == "DELETE":
    runner = template_requests.Delete(requests_count, template_dir)
    runner.send_request()
elif method == "PATCH":
    runner = template_requests.Patch(requests_count, template_dir)
    runner.send_request()

stop_time = time.time() - start

runner.save_stats()
print("Time elapsed: {} seconds".format(stop_time))
