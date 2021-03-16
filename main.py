import sys
import time
import utils

requests_count = int(sys.argv[1])
url = sys.argv[2]
method = sys.argv[3]

start = time.time()

if method == "GET":
    utils.get_request(requests_count, url)
elif method == "POST":
    utils.post_request(requests_count, url)


stop_time = time.time() - start

#utils.show_stats()
utils.save_stats()
print("Time elapsed: {} seconds".format(stop_time))
