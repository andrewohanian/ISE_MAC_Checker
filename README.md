# ISE_MAC_Checker
Web-based Tool to Verify Whether MAC Addresses Exist in the ISE Database

## Installation
* Clone the repo on your webserver or localhost
    * ```git clone https://github.com/andrewohanian/ISE_MAC_Checker.git```
* Change directory and install requirements
    * ```cd ISE_MAC_Checker
    * ```pip install -r requirements.txt```
## Quick-start
* Open ise_mac_search.py, and edit the username, password, and base_url
* Open ise_mac_check_app.py, and edit the approved_devices list with the names of the groups in your environment that you place approved MACs into
    * To find the group names in ISE:
        * Work Centers -> Network Access -> Id Groups -> Endpoint Identity Groups
* Run ise_mac_check_app.py, and browse to http://mywebserver.com:5000 or http://localhost:5000
![example](https://i.imgur.com/xUstFN2.png)
