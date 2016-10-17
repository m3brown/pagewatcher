import os
from flask import Flask
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)

URL = 'http://barexam.virginia.gov/bar/barresults.html'
WAYBACK_URL = 'https://web.archive.org/web/20151101161538/http://barexam.virginia.gov/bar/barresults.html'

@app.route('/')
def pagewatcher():

    r = requests.get(WAYBACK_URL)
    soup = BeautifulSoup(r.text)

    mydivs = soup.findAll("div", { "class" : "panel-success" })

    if len(mydivs) > 0:
        return "GOT RESULTS!!"
    else:
        return "NO RESULTS :("
