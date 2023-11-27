from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from bs4 import BeautifulSoup as bs

import json
import requests
import mysql.connector

db = mysql.connector.connect(
	host="localhost",
	user="stadioner",
	password="stadionpass",
	database="Stadion_2"
)

db_cursor = db.cursor()

"""
class Afisha:
        data = []
        def __init__(self):
                soup = bs(requests.get('https://ticketon.kz/sports'))
                tmp = soup.find_all("div", {"class": "block-1 list-block"})
                for match in tmp:
                        data.append(match.find("span", {"class": "list-item__date"}))
"""

def getMedia():
	db_cursor.execute("SELECT * FROM images;")
	return db_cursor.fetchall()

# Create your views here.
def indexPage(request):
    template = loader.get_template('index.html')
#    afisha = Afisha()
    images = getMedia()
    dataset = {"title": "Stadion", "media":images}
    return HttpResponse(template.render(context=dataset))
