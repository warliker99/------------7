
import requests
import json


class Connection_r7(requests.Request):
	def __init__(self, url_login: str, headers: dict, data: dict):
		self.__url_login = url_login
		self.__headers = headers
		self.__data = data
		self.__login_token = {}
	
		req = super().__init__(url=self.__url_login, json=self.__data, headers=self.__headers)
	
		self.__login_token = json.loads(req.text)
		self.__login_token = login_token['Response']['Data']['Tokens']['AuthToken']

    
	def upload_dirs(self, url_upload_dirs: str):
   		data_mkdir = {
        "Name": self.name,
        "Description": self.name,
        "Order": 100,
        "Type": "Default",
        "IconId": None,
        "RoleIds": [],
        "UserIds": [],
        "ParentId": self.parent_id }
    
	#	req_mkdir = supper().__init__(url=url_upload_dirs, json=data_mkdir, headers=self.headers)
    