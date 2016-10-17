import os
from flask import Flask, send_file
from selenium import webdriver  

app = Flask(__name__)

URL=http://barexam.virginia.gov/bar/barresults.html
WAYBACK_URL=https://web.archive.org/web/20151101161538/http://barexam.virginia.gov/bar/barresults.html

@app.route('/')
def pagewatcher():

    driver = webdriver.PhantomJS()
    driver.set_window_size(1024, 768) 
    driver.get(URL)
    driver.save_screenshot('screen.png') 
    driver.quit()

    return send_file('screen.png', mimetype='image/png')
