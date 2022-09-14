#!/usr/bin/env python3
"""Shows a web page where you can apply for a job"""
import json

from flask import Flask, request
import sqlite3, requests
import os.path

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def hello():
    with open('resources/job_application.html', 'r') as fp:
        data = fp.read()
    return data


@app.route("/apply_for_job", methods=["POST"])
def apply():
    pass

def execute_db_query(query, params=None):
    assert query is not None
    dbcon = sqlite3.connect(dbfile)

    cur = dbcon.cursor()
    if params is not None:
        cur.execute(query,params)
    else:
        cur.execute(query)

    dbcon.commit()
    dbcon.close()


def encrypt_data(data):
   pass

cert_file_path = "./resources/client.cert.pem"
key_file_path = "./resources/client.key.pem"
api_url = "https://localhost:5001"

resp = requests.post(api_url+"/create_user", cert=(cert_file_path, key_file_path), verify=False)
assert 200 <= resp.status_code <= 299 , "Could not create user"
userid = int(json.loads(resp.text)["key_id"])
dbfile = "/tmp/bewerbungen.db"

if not os.path.exists(dbfile):
    execute_db_query('''<Hier Create Table statement einfügen>''', None)

app.run(ssl_context='adhoc', host="0.0.0.0", port=443 , debug=False)

