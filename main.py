from connection_r7 import *
import json
from powershell import *



def __main__():
    with open('C:\\Users\\Alex\\Nextcloud\\Мигратор в р7\\config.json', 'r', encoding='utf-8') as file:
       json_config = json.load(file)
       pass
    
    headers = {'Content-Type': 'application/json'}
    
    data = {
  "Login": json_config['R7_USER_ADMIN'],
  "LoginAs": None,
  "Password": json_config['R7_USER_ADMIN_PASSWORD'],
  "PasswordHash": None,
  "CryptedPassword": ""
  }
    
  #r7_login_token = Connection(url=json_config['R7_URL_LOGIN'], json = data, headers = headers)
    ps = powershell_connection(json_config['PS_FQDN_SERVER'],json_config['PS_USER'],json_config['PS_USER_PASSWORD'])
    ps.get_permissons(json_config['PATH_TO_SCRIPT_ACL'])

__main__()
