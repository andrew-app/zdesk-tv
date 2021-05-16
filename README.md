# zdesk-tv
A python CLI app for viewing customer support tickets. The App requests tickets from the [Zendesk](https://www.zendesk.com/) Ticket API and displays them to the user. It pages the ticket list 25 at a time. Currently configured with my personal zendesk account. 
 

# Setup
1. Clone repository. 
2. Install required dependencies. `$ pip3 install -r requirements.txt`
3. Navigate to folder. `$ cd path/to/repo` 
4. Run the setup script to add credentials for authentication. `$ python3 setup.py`
5. Run main script to view tickets `$ python3 main.py`

# Usage

* To view details of a single ticket `>>>-t <ticket # ID>`

![Alt Text](ticket1.gif)

* To list tickets for a specific page `>>>-p <page_number>`

![Alt Text](ticket-list.gif)


