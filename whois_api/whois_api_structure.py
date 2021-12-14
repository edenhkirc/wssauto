import requests 
import json 

'''
	1. Load JSON of Domain Values
	2. Get Responses
	3. Return Status
	4. Test Response fields

'''

class WhoIsDomain():
	lang = "eng"
	inputType = "domain"
	response_time=0
	response = ''
	def __init__(self, dom: str, url: str):
		self.url = url
		self.domain = dom
		
	def get_response(self):
		payload = json.dumps(
		{
		    "clientIp": "172.11.81.173",
		    "lang": self.lang,
		    "input": {
			"type": self.inputType,
			"whoistext": self.domain
		    }
		})

		headers = {
		    'Content-Type': 'application/json'
		}

		response = requests.request("POST", self.url,
		    headers=headers, data=payload)

		self.response = response.text
		self.response_time = response.elapsed.microseconds
		
	
	def hasFourContacts(self):
		pass
	def hasValidEmail(self):
		pass
	def hasValidDoman(self):
		pass
	def hasValidPunyDomain(self):
		pass



