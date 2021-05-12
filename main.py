from tabulate import tabulate
import math
import json



with open('mytickets.json') as f: # load tickets locally stored
    x = json.load(f)

data = x['tickets']


tickets = len(data) # total tickets

headers = ["Ticket # ID", "Subject", "Requester ID", "Creation Date"] #table headers

print("Type Ticket Number ID for individual ticket details.")
pages = math.floor(tickets/25)

print(f"Showing 25 of {tickets} tickets (1 of {pages} page(s)).")


# show table function
def listview(a, b):
    tid = []  # store ticket ID numbers
    subj = []  # store ticket subjects
    rid = []  # store requester IDs
    crdate = []  # creation dates

    for i in range(a, b):
        tid.append(data[i]['id'])
        subj.append(data[i]['subject'])
        rid.append(data[i]['requester_id'])
        crdate.append(data[i]['created_at'])

    table = zip(tid, subj, rid, crdate) #index elements from each category

    print(tabulate(table, headers, tablefmt="fancy_grid")) #shows table


start = 0

stop = 25

listview(start, stop)

