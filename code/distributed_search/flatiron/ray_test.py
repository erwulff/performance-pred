"""
code from: https://docs.ray.io/en/latest/cluster/quickstart.html
"""

import socket
import time
from collections import Counter

import ray

ray.init(address="auto")

print(
    """This cluster consists of
    {} nodes in total
    {} CPU resources in total
""".format(
        len(ray.nodes()), ray.cluster_resources()["CPU"]
    )
)


@ray.remote
def f():
    time.sleep(0.001)
    # Return IP address.
    return socket.gethostbyname(socket.gethostname())


object_ids = [f.remote() for _ in range(10000)]
ip_addresses = ray.get(object_ids)

print("Tasks executed")
for ip_address, num_tasks in Counter(ip_addresses).items():
    print("    {} tasks on {}".format(num_tasks, ip_address))
