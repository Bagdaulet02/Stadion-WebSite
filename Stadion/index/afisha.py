import json
import requests
from bs4 import BeautifulSoup as bs

class Afisha:
	data = []
	def __init__(self):
		soup = bs(requests.get('https://ticketon.kz/sports'))
		tmp = soup.find_all("div", {"class": "block-1 list-block"})
		for match in tmp:
			data.append(match.find("span", {"class": "list-item__date"}))
