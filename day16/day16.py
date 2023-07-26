import re
from functools import lru_cache
lines = open("in.txt").readlines()

valvemap = dict()

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_generator():
    count = 0
    num = 2
    while count < 60:
        if is_prime(num):
            yield num
            count += 1
        num += 1

prime_map = dict()

generator = prime_generator()


def extract_information(line):
    pattern = r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'
    match = re.match(pattern, line)

    if match:
        valve_name = match.group(1)
        flow_rate = int(match.group(2))
        tunnels_leads_to = match.group(3).split(', ')

        return valve_name, flow_rate, tunnels_leads_to
    else:
        return None

for line in lines:
    extracted_info = extract_information(line)
    if extracted_info:
        valve_name, flow_rate, tunnels_leads_to = extracted_info
        valvemap[valve_name] = (flow_rate, tunnels_leads_to)
        prime_map[valve_name] = next(generator)


@lru_cache(maxsize = None)
def search(time, node, visited : int):
    ans = 0
    if time == 0:
        return 0
    if visited % prime_map[node] != 0 and valvemap[node][0] >0:
        visitedcopy =  visited * prime_map[node]
        ans = max(ans, (time - 1) * valvemap[node][0] + search(time - 1, node, visitedcopy))
    for nbor in valvemap[node][1]:
        ans = max(ans, search(time - 1, nbor, visited))
    return ans

print(search(30, "AA", 541))