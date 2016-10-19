from django.conf import settings
import logging
import requests

from bs4 import BeautifulSoup
import requests
from postmark import PMMail, PMBatchMail

from core.models import Watch, Page

logger = logging.getLogger(__name__)

def cron():
    logger.info("Running watcher.cron")

    pages = Page.objects.all()
    for page in pages:
        watches = Watch.objects.filter(page=page).filter(triggered=False)
        if len(watches) > 0:
            grep_page(page, watches)


def grep_page(page, watches):
    logger.info("Beginning query of %s" % page.url)

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(page.url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    mydivs = soup.findAll("div", {"class": "panel-success"})

    if len(mydivs) > 0:
        logger.info("Found match for %s" % page.url)
        page.triggered = True
        page.save()
        send_emails(watches, page)
        return True
    else:
        return False


def send_emails(watches, page):
    for watch in watches:
        logger.info("Sending email to %s for url %s" % (watch.email, page.url))
        PMMail(api_key=settings.POSTMARK_API_TOKEN,
               subject="The VA Bar Results have been released!!",
               sender=settings.POSTMARK_SENDER_EMAIL,
               to=watch.email,
               text_body="Click here to see the bar results: %s" % page.url,
               html_body="Click <a href='%s'>here</a> to see the bar results" % page.url).send()
        watch.triggered=True
        watch.save()
