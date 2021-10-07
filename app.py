from flask import Flask
import boto3
import os
from opensearchpy import OpenSearch


app = Flask(__name__)

session = boto3.Session(profile_name='default')

host = ''
port = 9200

client = OpenSearch(
    hosts = [{'host': host, 'port': port}]

)

@app.route("/contacts")
def get_contacts():
    # Search for the document.
    index = 'contacts'
    body = {
    'query': {
        'match_all': {}
    }
    }

    response = client.search(
        body = body,
        index = index
    )
    return response

@app.route("/contacts/<contacts_id>")
def get_contacts():
    # Search for the document.
    index = 'contacts'
    body = {
    'query': {
        'match': {
            "contacts_id": { query: contacts_id}
        }
    }
    }

    response = client.search(
        body = body,
        index = index
    )
    return response

