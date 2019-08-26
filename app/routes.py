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
import pickle #for developement purposes
from operator import itemgetter #for sort function


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
    return render_template('results_social_rank.html', page="RECIPES")

# Find recipes with ML model
"""
@app.route('/test')
def test():
    return render_template('ML.html', page="ML")
"""

@app.route('/404')
def error():
    return render_template('404.html', page="ERROR 404")

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


def sortRecipes(rank_type,recipes_data):
    if(rank_type == 'social_rank'):
        recipes_data.sort(key=lambda x: int(x[1]))
        recipes_data.reverse()
        for recipe in recipes_data:
            recipe[7] = recipe [1]
            # print(recipe[1])
    else:
        recipes_data.sort(key=lambda x: int(x[6]))
        recipes_data.reverse()
        for recipe in recipes_data:
            recipe[7] = recipe [6]
            # print(recipe[6])
        
    
    return recipes_data


recipes_data = []
@app.route('/processListOfFoods', methods=['POST'])
def processListOfFoods():
    global recipes_data
    listOfFoods = []
    for i in request.form:
        listOfFoods.append(request.form[i])
    recipes_data = ws.Scraper(listOfFoods, 30, 1).scrape()

        # with open("recipes_data.txt","wb") as fp:
    #     pickle.dump(recipes_data,fp)

    # with open("recipes_data.txt", "rb") as fp:   # Unpickling
    #     recipes_data = pickle.load(fp)

    if recipes_data == None:
        return render_template('404.html', page="ERROR 404")



    recipes_data = ML.assignMLranking(recipes_data)

    #default display_rank would be social
    for recipe in recipes_data:
        recipe.append(recipe[1])

    # print(recipes_data)
    return render_template('results_social_rank.html', page="RECIPES", data=recipes_data, error=False) # redirect to new page with recipes

@app.route('/sortListOfFoods', methods=['POST'])
def sortListOfFoods():
    global recipes_data
    htmlPage = 'results_social_rank.html'
    rank_type = "social_rank"
    # print(request.form['rank'])

    if(request.form['rank'] == 'rank_op_2'):
        rank_type = "ml_rank" 
        htmlPage = 'results_ml_rank.html'
    
    sorted_recipes_data = sortRecipes(rank_type,recipes_data)

    

    
    return render_template(htmlPage, page="RECIPES", data=sorted_recipes_data , error=False) # redirect to new page with recipes









# Create recipes with machine learning model and assigns given score to each model (the higher the score the better)
@app.route('/recipe/<filename>')
def recipe(filename):
    # ML.run()
    return redirect(url_for('index'))

def write_to_file(text, filename):
    file = open(filename, "w")
    file.write(text)
    file.close()


app.run(debug=True)


# export FLASK_ENV=development