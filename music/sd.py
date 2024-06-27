import requests
import json

ret = requests.get("http://localhost:4000/playlist/detail", params={'id': 372423538}).json()
# ret = ret['playlist']
for x in list(ret.keys()):
    print('{}: {}'.format(x, len(json.dumps(ret[x]))))
    # print(json.dumps(ret[x]))

