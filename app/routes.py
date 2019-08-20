import os
from app import app
from os.path import join, dirname, realpath
import requests
from flask import request, redirect, url_for, render_template, flash, send_from_directory
from werkzeug.utils import secure_filename
import sys
from bs4 import BeautifulSoup
sys.path.append("..") # Appends directory
import ml # Import ml model file
import web_scraper

# Route all of our functions to URL
@app.route('/')
@app.route('/index')
def hello(filename="", error=""):
    return render_template('index.html', filename=filename, error=error)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

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
@app.route('/parse')
def parse():
    return redirect(url_for('index'))

# Create recipes with machine learning model and assigns given score to each model (the higher the score the better)
@app.route('/recipe/<filename>')
def recipe(filename):
    return redirect(url_for('index'))
    # ml.run()

def write_to_file(text):
    file = open("testfile.txt", "w")
    file.write(text)
    file.close()

app.run(debug=True)