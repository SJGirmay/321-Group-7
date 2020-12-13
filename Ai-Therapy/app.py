# The sources we used are:
# https://dev.to/sahilrajput/build-a-chatbot-using-flask-in-5-minutes-574i
# https://www.studytonight.com/post/create-a-javascript-covid-19-tracker


#import files
from flask import Flask, render_template, request, redirect, url_for
import requests
import os
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import InputRequired, Length, AnyOf
from flask_bootstrap import Bootstrap
import bs4
from bs4 import BeautifulSoup
import pandas as pd
import time

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = 'SuperSecret'

#bot = ChatBot("Candice")
#trainers = ListTrainer(bot)
#trainers.train("chatterbot.corpus.english")

import json

data = json.loads(open('intents.json', 'r').read())
data1 = []

for intent in data["intents"]:
	for pattern in intent["patterns"]:
		data1.append(pattern)
	for response in intent["responses"]:
		data1.append(response)

from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Create a new chatbot name Lily
bot = ChatBot('Lily')

trainers = ListTrainer(bot)

trainers.train(data1)

@app.route('/AI')
def AI():    
    return render_template("AIchatbot.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')    
    return str(bot.get_response(userText)) 

class JobSearchForm(Form):
    eligible = StringField('Do you live in US', validators=[InputRequired()])
    keyword = StringField('Enter the type of job you are looking for', validators=[InputRequired()])
    state = StringField('What state do you live in', validators=[InputRequired()])

@app.route('/index', methods=['GET', 'POST'])
def index():
    form = JobSearchForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            country = request.form['eligible']
            job = request.form['keyword']
            location = request.form['state']
            URL = URLGen(country, job, location)
            pageUrls = PageGen(URL)

            for page in pageUrls:
                #print("Page " + str(x))
                return findJobs(page)

    return render_template("index.html", form=form)

def URLGen(country, job, location):
    URL_Job = "+".join(job.split())
    URL_Location = "+".join(location.split())


    if country == 'Yes':
        URL = "https://www.indeed.com/jobs?q="+str(URL_Job)+"+24"+"%2C000&l="+str(URL_Location)
    elif country == 'yes':
        URL = "https://www.indeed.com/jobs?q=" + str(URL_Job) + "+24" + "%2C000&l=" + str(URL_Location)
    else:
        URL = ''
        print("sorry we only offer options for people in the US.")


    return(URL)

def PageGen(URL):
    pageUrls = []
    for x in range(10, 40, 10):
        pageUrls.append(URL+"&start="+str(x))
    return pageUrls

def findJobs(URL):
    if URL != '':
        #conducting a request of the stated URL above:
        # print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.text, "html.parser")
        # print(soup.prettify())

        jobs = job_title_result(soup)
        locations = location_result(soup)

        # sumamries = summary_result(soup)

        string_final = '%-10s%-60s%s'
        loclist = []
        # print(string_final % ('', 'Job title', 'Location', 'salary'))
        for i, (job, location) in enumerate(zip(jobs, locations)):
            loclist.append(string_final % (i, job, location))
        return render_template('joblist.html', loclist=loclist)

def summary_result(soup):
    summaries = []
    spans = soup.find_all("span", attrs={"class":"summary"})
    for span in spans:
        summaries.append(span.text.strip())
    return(summaries)

def location_result(soup):
    locations = []
    spans = soup.find_all("span", attrs={"class": "location"})
    for span in spans:
        locations.append(span.text)
    return(locations)

def job_title_result(soup):
    jobs = []
    for div in soup.find_all(name="div",attrs={"class":"row"}):
        for a in div.find_all(name="a",attrs={"data-tn-element":"jobTitle"}):
            jobs.append(a["title"])
    return(jobs)


@app.route('/covid/')
def covid():
    userText = request.args.get('msg')
    worldwide_data_url = "https://corona.lmao.ninja/v2/all"
    worldwide_content = requests.get(worldwide_data_url)
    worldwide_data = worldwide_content.json()
    return render_template("covid.html", data=worldwide_data)

if __name__ == "__main__":    
    app.run(host="0.0.0.0")

