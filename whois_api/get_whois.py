import requests 
import logging
import random
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler
from whois_api_structure import WhoIsDomain

UAT_SITE = 'http://uatservice.hkirc.hk/api/whois'
PROD_SITE = "https://service.hkirc.hk/api/whois"

DOMAIN_FILE = 'domain_lookup.txt'

PATH = '/Users/eden.ho/Documents/CyberSecurity/VSCode/whois_api'

def setup_logging(name, file_name, level=logging.INFO):
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	handle = logging.FileHandler(file_name, mode='w',encoding='utf-8', delay=False)
	handle.setFormatter(formatter)
	logger = logging.getLogger(name)
	logger.setLevel(level)
	logger.addHandler(handle)
	return logger

def try_whois(domains):
	for dom in domains:
		# uat_logger = setup_logging('uat_logger',datetime.now().strftime(PATH+'/uat/whoisUAT_%d_%m_%Y.log'))
		prod_logger = setup_logging('prod_logger',datetime.now().strftime(PATH+'/prod/%Y-%m-%d-{}.log').format(dom))

		#Get status code
		try:
			# uat_status = requests.post(UAT_SITE).status_code
			production_status = requests.post(PROD_SITE).status_code
		except Exception as e:
			print('Get Status Code Error')
			# uat_logger.debug('UAT Status Code Error: ' + str(e))

			prod_logger.debug('Production Status Code Error: ' + str(e))
		else:
			# uat_logger.info('UAT Status Code: ' + str(uat_status))

			prod_logger.info('Production Status Code: ' + str(production_status))

		#Get next domain
		try:
			# whois_uat = WhoIsDomain(dom=dom, url=UAT_SITE)
			# whois_uat.get_response()

			whois_prod = WhoIsDomain(dom=dom, url=PROD_SITE)
			whois_prod.get_response()

		except Exception as e:
			print('Get Domain Error')
			# uat_logger.debug('Get Response Time Error: '+ str(e))
			# uat_logger.debug('Get Response Error: '+ str(e))

			prod_logger.debug('Get Response Time Error: '+ str(e))
			prod_logger.debug('Get Response Error: '+ str(e))	
		else:
			# uat_logger.info('Domain: '+ str(whois_uat.domain))
			# uat_logger.info('Response Time (microseconds): '+ str(whois_uat.response_time))
			# uat_logger.info('Response: '+ str(whois_uat.response))

			prod_logger.info('Domain: '+ str(whois_prod.domain))
			prod_logger.info('Response Time (microseconds): '+ str(whois_prod.response_time))
			prod_logger.info('Response: '+ str(whois_prod.response))

		# uat_logger.handlers.clear()
		prod_logger.handlers.clear()

if __name__ == "__main__":
	with open(DOMAIN_FILE,'r',encoding='utf-8') as file:
		wholeFile = file.read()

		domains = list(map(str,wholeFile.split()))
		try_whois(domains)