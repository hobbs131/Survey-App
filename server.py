from flask import Flask, render_template, request, g, redirect, url_for, jsonify
from datetime import datetime
import db, time

app = Flask(__name__)

# have the DB submodule set itself up before we get started. groovy.
@app.before_first_request
def initialize():
    db.setup()

@app.route('/')
def root():
    return render_template("root.html")

@app.route('/survey')
def survey():
    return render_template("survey.html")

@app.route('/decline')
def decline():
    return render_template("decline.html")

@app.route('/thanks')
def thanks():
    return render_template("thanks.html")

@app.route('/surveyResults', methods=['POST'])
def serveyResults():
    with db.get_db_cursor(True) as cur:
       
        input_ = request.form.get('input')
        radio_button = request.form.get('gender')
        select_box = request.form.get('numbers')
        checkbox = request.form.get('checkbox')
        ts = datetime.now()

        cur.execute("INSERT INTO survey_responses (input, radio_button, select_box, checkbox, ts) VALUES (%s,%s,%s,%s,%s)", (input_, radio_button, select_box, checkbox, ts,))
        return render_template("thanks.html")
    
@app.route('/api/results')
def api_results():
    param = request.args.get("reverse")

    with db.get_db_cursor(True) as cur:
        cur.execute("SELECT json_agg(survey_responses) FROM survey_responses")
        results = cur.fetchone()[0]

        if (param == "true"):
            results.reverse()

        data = {
        "results" : results
        } 
        return data