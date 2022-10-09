#!/usr/bin/env python3
import json
import requests
from requests.auth import HTTPBasicAuth
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import urllib.parse




token_url = 'https://api.otto.market/v1/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache'}

data = {'username': '',
        'password': '',
        'grant_type': 'password',
        'client_id': 'token-otto-api'}

data_encoded = urllib.parse.urlencode(data)


req = requests.request(method='POST',
        url=token_url,
        headers=headers,
        data=data_encoded)

print(req.content)

