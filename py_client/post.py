import requests
from tinydb import TinyDB

url = 'http://127.0.0.1:8000/'

db = TinyDB('db.json')

all_tables = db.tables()

for i in all_tables:

    table = db.table(i)

    for j in table:
        r = requests.post(url, data=j)

