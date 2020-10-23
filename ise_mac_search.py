import requests
import json
requests.packages.urllib3.disable_warnings()

username = 'admin'
password = 'password'
base_url = 'https://ise.mydomain.com:9060/ers/config'
auth = (username, password)
headers = {'Accept': 'application/json'}

def get_rejected_endpoints():
    '''
    Returns a list of all currently rejected endpoints
    '''

    url = f'{base_url}/endpoint/getrejectedendpoints'

    response = requests.request("GET", url, auth = auth, headers=headers, verify=False)
    result = json.loads(response.text)

    return [i['value'] for i in result['OperationResult']['resultValue']]
    

def get_endpoints(mac):
    '''
    Returns the link to the endpoint object of interest, by searching all endpoints and filtering 
    on the MAC
    '''

    url = f'{base_url}/endpoint?filter=mac.EQ.{mac}'
	
    response = requests.request("GET", url, auth = auth, headers=headers, verify=False)

    result = json.loads(response.text)
    try:
        return result['SearchResult']['resources'][0]['link']['href']
    except:
        return False

def get_group_id(url):
    '''
    Returns the group ID the endpoint belongs to
    '''

    response = requests.request("GET", url, auth = auth, headers=headers, verify=False)

    result = json.loads(response.text)
    return result['ERSEndPoint']['groupId']


def get_group(group_id):
    '''
    Returns the name of the endpoint group
    '''

    url = f'{base_url}/endpointgroup/{group_id}'

    response = requests.request("GET", url, auth = auth, headers=headers, verify=False)

    result = json.loads(response.text)
    return result['EndPointGroup']['name']





