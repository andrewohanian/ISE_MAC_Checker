from flask import Flask, render_template, request
from ise_mac_search import get_endpoints, get_group_id, get_group, get_rejected_endpoints
import re

app = Flask(__name__)
#result=''
approved_groups = ['Phones', 'Printers', 'Video_Camers', 'IoT']

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/send', methods=['POST'])
def send(result=result):
    if request.method == 'POST':
        #Obtain the MAC submitted through the web form
        mac = request.form['mac']
        
    #Check if MAC is formatted properly
    if re.match(r"^([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})$", mac):
        #Check if MAC is rejected first
        rejected_endpoints = get_rejected_endpoints()
        if mac in rejected_endpoints:
            return render_template('home.html', result=f'MAC {mac} is currenty in a rejected state.', return_error=True)

        #If MAC is not rejected, check if it exists in an approved group
        else:
            endpoint_link = get_endpoints(mac=mac)
        
        if endpoint_link:
            group_id = get_group_id(endpoint_link)
            group_name = get_group(group_id)

            if group_name not in approved_groups:
                return render_template('home.html', result=f'No match for [{mac}]. Please submit a ticket to add it to the database of approved devices.')
            else:
                print(f'Match found, {mac} exists in group: {group_name}')
                return render_template('home.html', result=f'MAC Found: [{mac}] exists in group [{group_name}]')
    
        else:
            print(f"No match for {mac}")
            return render_template('home.html', result=f'No match for [{mac}]. Please submit a HEAT ticket to add it to the database of approved devices.')
    else:
        return render_template('home.html', result='Failed MAC formatting check. Please format MAC as 01:23:45:67:89:AB', return_error=True)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

