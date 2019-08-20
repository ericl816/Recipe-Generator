""" TO DO:
- Insert into routes.py
- Parse JSON results
- Feed parsed results into ML model
 """
import requests
from bs4 import BeautifulSoup

API_KEY = 'apiKey=e94b15c6de0f48798c858f4c88a9d4ed'

class Scraper:
	def __init__(self, food, num_recipes):
		self.food = food
		self.score = 0

		ingredients = food.split()
		l = []
		for i in range(len(ingredients)):
			print(ingredients[i])
			if i == 0:
				l.append(ingredients[i])
			else:
				l.append(',+' + ingredients[i])
		s = ''.join(l)

		payload = {
	        'fillIngredients': False,
	        'ingredients': s,
	        'limitLicense': False,
	        'number': num_recipes,
	        'ranking': 1
	    }

		self.url = 'https://api.spoonacular.com/recipes/findByIngredients?ingredients={}'.format(s) + num + '&ranking=1'
		print(self.url)
		# https://spoonacular.com/food-api/docs#Search-Recipes-by-Ingredients

	def run (self):
		response = requests.get(self.url)
		print(response.text)
		soup = BeautifulSoup(response.text, 'html.parser')

s = Scraper('pizza pasta cake', 3)
s.run()