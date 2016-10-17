import os
from flask import Flask
from bs4 import BeautifulSoup
import requests
import os
from postmark import PMMail, PMBatchMail


app = Flask(__name__)

URL = 'http://barexam.virginia.gov/bar/barresults.html'
WAYBACK_URL = 'https://web.archive.org/web/20151101161538/http://barexam.virginia.gov/bar/barresults.html'

POSTMARK_SENDER_EMAIL = os.environ.get('POSTMARK_SENDER_EMAIL')

@app.route('/')
def pagewatcher():

    r = requests.get(WAYBACK_URL)
    soup = BeautifulSoup(r.text)

    mydivs = soup.findAll("div", {"class": "panel-success"})

    if len(mydivs) > 0:
        messages = list(create_emails())
        to_send = PMBatchMail(messages=messages)
        to_send.send(test=False)
        return "GOT RESULTS!!"
    else:
        return "NO RESULTS :("


def create_emails():
    for email in ['test@gmail.com', 'test2@gmail.com']:
        yield PMMail(api_key=os.environ.get('POSTMARK_API_TOKEN'),
                     subject="The VA Bar Results have been released!!",
                     sender=POSTMARK_SENDER_EMAIL,
                     to=email,
                     text_body="Click here to see the bar results: %s" % URL,
                     tag="bar-results")
