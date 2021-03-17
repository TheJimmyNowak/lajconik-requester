import random
import string


def get_random_str(min_length=0, max_length=255):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in
                   range(random.randint(min_length, max_length)))
