from flask import Flask, request, Markup, render_template, flash, Markup
import os
import json

app = Flask(__name__)

@app.route("/")
def render_main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    return render_template('start.html', options=get_state_options(counties))
def get_state_options(counties):
    options=""
    listOfStates=[]
    for x in counties:
        if x["State"] not in listOfStates:
            listOfStates.append(x["State"])
    for x in listOfStates:
        options += Markup("<option value=\"" + x + "\">" + x + "</option>")
    return options

if __name__=="__main__":
    app.run(debug=True, port=54321)