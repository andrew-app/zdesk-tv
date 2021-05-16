from getpass import getpass

import pickle

import json

import requests

from requests.auth import HTTPBasicAuth


subdomain = input("Enter Subdomain: ")

username = input("Enter username/email: ")

password = getpass()


url = f"https://{subdomain}.zendesk.com/api/v2/tickets"



response = requests.get(url, auth=HTTPBasicAuth(username, password))

data = response.json()

try:
    output = data['error']
    print("Authentication Error, Check Credentials and Try Again.")

except KeyError:
    creds = {"subd" : subdomain, "usrn" : username, "pw" : password}

    pickle.dump(creds, open("creds.p", "wb"))


    print("Authentication successful, Credentials Stored.")
