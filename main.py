from datetime import datetime
from flask import Flask, render_template, make_response, Markup
from google.cloud import datastore

datastore_client = datastore.Client(project='howfullismywall')

#work out todays date
x = datetime.now()
today = x.strftime("%A") + " " + x.strftime("%e") + " " + x.strftime("%B")

app = Flask(__name__)

#function to get the treatments from the db
def fetch_counters(filter, operator):
    query = datastore_client.query(kind='counters')
    if filter != "":
        query.add_filter('city', operator, filter)
    #query.order = ['-timestamp']

    counters = query.fetch()

    return counters

@app.route('/')
@app.route('/index')
def root():
    filter = ""
    operator = "="
    counters = fetch_counters(filter, operator)
    return render_template('index.html', today=today, title="Home", heading="All counters", counters=counters)

@app.route('/sheffield')
def sheffield():
    filter = "sheffield"
    operator = "="
    counters = fetch_counters(filter, operator)
    return render_template('index.html', today=today, title="Sheffield", heading="Sheffield", counters=counters)

@app.route('/manchester')
def manchester():  
    filter = "manchester"
    operator = "="
    counters = fetch_counters(filter, operator)  
    return render_template('index.html', today=today, title="Manchester", heading="Manchester", counters=counters)

@app.route('/leeds')
def leeds():
    filter = "leeds"
    operator = "="
    counters = fetch_counters(filter, operator)
    return render_template('index.html', today=today, title="Leeds", heading="Leeds", counters=counters)

@app.route('/london')
def london():
    filter = "london"
    operator = "="
    counters = fetch_counters(filter, operator)
    return render_template('index.html', today=today, title="London", heading="London", counters=counters)

@app.route('/others')
def others():
    filter = ""
    operator = "="
    counters = fetch_counters(filter, operator)
    return render_template('index.html', today=today, title="Others", counters=counters)

@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html', title="How full is my wall? 10 Popular Questions", metadesc="Answers to the 10 most commonly asked questions about how full my wall is")

@app.route("/sitemap.xml")
def sitemap_xml():
    response = make_response(render_template("sitemap.xml"))
    response.headers['Content-Type'] = 'application/xml'
    return response

@app.route("/robots.txt")
def robots_txt():
    return render_template("robots.txt")

@app.route("/security.txt")
def security_txt():
    return render_template("security.txt")

if __name__ == '__main__':
    # This is used when running locally only. 
    app.run(host='127.0.0.1', port=8080, debug=True)