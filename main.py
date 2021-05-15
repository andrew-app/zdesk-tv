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

    str1 = ''.join(str(e) for e in p)

    try:

        val = int(str1)

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

    if test > 0:
        test2 = test - 1
        start = test2*25
        stop = start + 25
        print(f"Showing {start+1} to {stop} of {tickets} tickets. {test} of {pages} page(s)).")
        listview(start,stop)
    else:
        print(f"invalid ticket page (Min: 1, Max: {pages}).")

def show_ticket(ticket_number):
    print("ticket info")
 
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


