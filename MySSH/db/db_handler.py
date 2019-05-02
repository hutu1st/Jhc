import json
import os
from conf.settings import DB_PATH


def save(obj):
    path = os.path.join(DB_PATH, 'server.json')
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f)


def select():
    path = os.path.join(DB_PATH, 'server.json')
    with open(path, 'r', encoding='utf-8') as f:
        res = json.load(f)

    return res
