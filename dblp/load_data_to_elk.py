import requests

FILE = 'dblp-ref-0.json-00.json'
# {... single data ...}
# {... single data ...}

BACKEND = 'http://elastic:fdt@elk.local/index/_doc/'

HEADERS = {'content-type': 'application/json'}

with open(FILE, 'r') as f:
    for line in f.readlines()[:]:
        r = requests.post(BACKEND, data=line, headers=HEADERS)
        print(r.text)
