import os, time
from app import app
from os.path import join, dirname, realpath
import requests
from flask import request, redirect, url_for, render_template, flash, send_from_directory
from werkzeug.utils import secure_filename
import sys
from bs4 import BeautifulSoup
sys.path.append("..") # Appends directory
import ml as ML # Import ml model file
import web_scraper as ws

# Route all of our functions to URL
@app.route('/')
@app.route('/index')
def hello(filename="", error=""):
    return render_template('index.html', page="WELCOME")

@app.route('/about')
def about():
    return render_template('about.html', page="ABOUT")

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html', page="DISCLAIMER")

@app.route('/results')
def results():
    return render_template('results.html', page="RECIPES")

# Get food input from user in buttons
@app.route('/get_input', methods=['GET', 'POST'])
def get_input():
    if request.method == 'POST':
        try:
            # https://stackoverflow.com/questions/47083403/extracting-input-from-all-input-boxes-into-a-list-using-flask
            values = request.form.getlist('')
        except Exception as e:
            return render_template('index.html', error=e)
    return redirect(url_for('index'))

# Parse food info with BeautifulSoup
@app.route('/parse', methods = ['GET', 'POST'])
def parse():
    if request.method == 'POST':
        result = handle(request.get_json())
        return jsonify(data=result)
    return redirect(url_for('index'))

@app.route('/processListOfFoods', methods=['POST'])
def processListOfFoods():
    listOfFoods = []
    for i in request.form:
        listOfFoods.append(request.form[i])
    recipes_data = ws.Scraper(listOfFoods, 5).scrape()
    for title, social_rank, image_url, source_url in recipes_data:
        print(title)
        print(social_rank)
        print(image_url)
        print(source_url)
    return render_template('results.html', page="RECIPES", data=recipes_data) # redirect to new page with recipes

# Create recipes with machine learning model and assigns given score to each model (the higher the score the better)
@app.route('/recipe/<filename>')
def recipe(filename):
    # ML.run()
    return redirect(url_for('index'))

def write_to_file(text):
    file = open("testfile.txt", "w")
    file.write(text)
    file.close()

# export FLASK_ENV=development
