from tabulate import tabulate
import math
import json
import pickle
import requests
from requests.auth import HTTPBasicAuth

creds = pickle.load( open( "creds.p", "rb" ) )


url = f"https://{creds['subd']}.zendesk.com/api/v2/tickets"



response = requests.get(url, auth=HTTPBasicAuth(creds['usrn'], creds['pw']))

x = response.json()


data = x['tickets']

print("Welcome to the Zendesk Ticket Viewer.")

tickets = len(data) # total tickets



if tickets >= 25:
    start = 0

    stop = 25

elif tickets == 0:
    print("No tickets were detected.")
    exit()

else:
    start = 0

    stop = tickets


pages = math.floor(tickets/25)


extra = tickets%25

exp = False #extra page boolean

if extra != 0:
    pages = pages + 1

    exp = True


print("Use -h for help.")

print(f"Showing {start+1} to {stop} of {tickets} tickets. 1 of {pages} page(s)).")


# show table function
def listview(a, b):
    tid = []  # store ticket ID numbers
    subj = []  # store ticket subjects
    rid = []  # store requester IDs
    crdate = []  # creation dates


    for index in range(a, b):
        tid.append(data[index]['id'])
        subj.append(data[index]['subject'])
        rid.append(data[index]['requester_id'])
        crdate.append(data[index]['created_at'])

    headers = ["Ticket # ID", "Subject", "Requester ID", "Creation Date"] #table headers

    table = zip(tid, subj, rid, crdate) #index elements from each category

    print(tabulate(table, headers, tablefmt="fancy_grid")) #shows table

#Check if page exists for list_tickets
def validpage(p):


    try:

        val = int(p)

        if val > pages:
            val = 0

        return val
    except ValueError:
        val = 0
        return val




# Display helpful commands to user
def help(r):
    print("These are the available commands:")
    print(f"-p <page_number> = view ticket page.")
    print(f"-t <ticket_number> = view individual ticket details.")
    print("exit = Terminate session")

#List tickets page
def list_tickets(page_number):

    test = validpage(page_number)

    if test > 0 and exp is False:
        test2 = test - 1
        start = test2*25
        stop = start + 25

        print(f"Showing {start+1} to {stop} of {tickets} tickets. {test} of {pages} page(s)).")
        listview(start,stop)

    elif test == pages and exp is True:
        if pages > 1:
            test2 = test - 1
            start = test2*25
            stop = start + extra
        else:
            start = 0
            stop = extra

        print(f"Showing {start+1} to {stop} of {tickets} tickets. {test} of {pages} page(s)).")
        listview(start,stop)
    else:
        print(f"Invalid ticket page (Min: 1, Max: {pages}).")
#Show individual ticket
def show_ticket(ticket_number):

    try:
        val = int(ticket_number)

        if val <= 0 or val > tickets:
            print(f"Invalid Ticket Number (Min: 1, Max: {tickets}).")
        else:
            print(f"Displaying details for ticket # {val}.")
            print(f"Subject: {data[val - 1]['subject']}")
            print(f"Requester ID: {data[val - 1]['requester_id']}")
            print(f"Created: {data[val - 1]['created_at']}")
            print(f"{data[val - 1]['description']}")

    except ValueError:
            print(f"Invalid Ticket Number (Min: 1, Max: {tickets}).")


commands = ["-h","-p","-t"]


# determines which function to excecute
exe = {0 : help,
       1 : list_tickets,
       2 : show_ticket
}
#At start up view first 25 tickets
listview(start, stop)


while 1:

    usrin = input(">>>")

    if usrin == "exit":
        print("Session Ended.")
        exit()

    arg = slice(2)
    cmd = usrin[arg]

    arg2 = slice(3,8) #4 bit buffer for correct input value
    inval = usrin[arg2]

    if cmd in commands:
        i = commands.index(cmd)
        exe[i](inval)

    else:
        print("Invalid command (use -h for help).")
