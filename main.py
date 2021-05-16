from tabulate import tabulate
import math
import json



with open('mytickets.json') as f: # load tickets locally stored
    x = json.load(f)

data = x['tickets']

print("Welcome to the Zendesk Ticket Viewer.")

tickets = len(data) # total tickets

if tickets == 0:
    print("No tickets were detected.")
    exit()


headers = ["Ticket # ID", "Subject", "Requester ID", "Creation Date"] #table headers



print("Use -h for help.")

pages = math.floor(tickets/25)

extra = tickets%25
exp = False

if extra != 0:
    pages = pages + 1

    exp = True

start = 0

stop = 25

print(f"Showing {start+1} to {stop} of {tickets} tickets. 1 of {pages} page(s)).")


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

def validpage(p):


    try:

        val = int(p)

        if val > pages:
            val = 0

        return val
    except ValueError:
        val = 0
        return val



commands = ["-h","-p","-t"]

def help(r):
    print("These are commands:")

def list_tickets(page_number):

    test = validpage(page_number)

    if test > 0 and exp is False:
        test2 = test - 1
        start = test2*25
        stop = start + 25

        print(f"Showing {start+1} to {stop} of {tickets} tickets. {test} of {pages} page(s)).")
        listview(start,stop)

    elif test == pages and exp is True:
        test2 = test - 1
        start = test2*25
        stop = start + extra

        print(f"Showing {start+1} to {stop} of {tickets} tickets. {test} of {pages} page(s)).")
        listview(start,stop)
    else:
        print(f"Invalid ticket page (Min: 1, Max: {pages}).")

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


exe = {0 : help,
       1 : list_tickets,
       2 : show_ticket
}

listview(start, stop)


while 1:

    usrin = input(">>>")

    if usrin == "exit":
        print("Session Ended.")
        exit()

    arg = slice(2)
    cmd = usrin[arg]

    arg2 = slice(3,5)
    inval = usrin[arg2]

    if cmd in commands:
        i = commands.index(cmd)
        exe[i](inval)
    else:
        print("Invalid command (use -h for help).")
