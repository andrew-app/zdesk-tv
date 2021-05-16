# zdesk-tv
A python CLI app for viewing customer support tickets. The App requests tickets from the [Zendesk](https://www.zendesk.com/) Ticket API and displays them to the user. It pages the ticket list 25 at a time. Currently configured with my personal zendesk account. 
 

# Setup
1. Clone repository
2. Install required dependencies using terminal command "pip install -r requirements.txt"
3. Navigate to folder `$ cd path/to/repo` 
4. Run the setup script to add credentials for authentication. `$ python3 setup.py`
5. Run main script to view tickets `$ python3 main.py`


To view details of a single ticket use command "-t <page_number>"

![Alt Text](ticket1.gif)
