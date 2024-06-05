import json
import os

conf = None

with open('conf.json', 'r', encoding='utf-8') as f:
    conf = json.loads(f.read())


def saveconf():
    with open(f"{os.path.dirname(os.path.dirname(os.path.realpath(__file__)))}/conf.json", 'w', encoding='utf-8') as f:
        f.write(json.dumps(conf, indent=4))

