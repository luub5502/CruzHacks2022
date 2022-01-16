from flask import Flask,render_template,request
from flask import url_for
#import pandas as pd
import random
from webScrape import scraper
app = Flask(__name__)
 
@app.route('/')
def form():
    return render_template('form.html')
@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        link = form_data["link"]
        articleTitleandText = scraper(link)
        return render_template('data.html',form_data = form_data)
"""@app.route('/About/')
def About():
    return render_template('About.html')
    """
app.run(host='localhost', port=5000)