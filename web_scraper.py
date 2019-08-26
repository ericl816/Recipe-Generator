import requests, sys, bs4, os, json
from collections import OrderedDict

# API_KEY = 'e3c679808020ba0a3aa594c8a2300160'
# API_KEY = 'e94b15c6de0f48798c858f4c88a9d4ed'
API_KEY = '4268c2c2835847dc035588f26ad36de6'

def scrape(listOfFoods):
    print('web scrape function called')
    listOfFoods.append('recipes')
    """for i in listOfFoods:
        print(i)"""
    myRequestURL = 'https://google.com/search?q='+",".join(listOfFoods)
    print(myRequestURL)
    res = requests.get(myRequestURL)
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    headlineResults = soup.find_all('a')

    for h in headlineResults:
        print(h)

class Scraper:
    def __init__(self, listOfFoods, num_recipes, sort_method):
        ingredients = ','.join(listOfFoods)
        self.num = num_recipes
        self.url = 'https://www.food2fork.com/api/search?key={0}&q={1}&sort=r'.format(API_KEY, ingredients) if sort_method == 1 else 'https://www.food2fork.com/api/search?key={0}&q={1}&sort=t'.format(API_KEY, ingredients)
        print(self.url)

    def scrape (self):
        print('calling API...')
        # E.g.: https://www.food2fork.com/api/search?key=e3c679808020ba0a3aa594c8a2300160&q=Eggs
        response = requests.get(self.url)
        data = json.loads(response.text)
        if 'error' in data and data['error'] == 'limit':
            print("50 call limit reached...")
            return None
        if data['count'] == 0:
            print("No recipe exists for given set of ingredients...")
            return None
        if data['count'] > 0:
            self.num = min(self.num, data['count']) # Limited to only 50 calls per day
        recipes = []
        # Return title, social ranking, image url, source_url, publisher_name, publisher_url for each recipe
        for i in range(self.num):
            rank = int(round(data['recipes'][i]['social_rank']))
            recipes.append([data['recipes'][i]['title'], str(rank), data['recipes'][i]['image_url'], data['recipes'][i]['source_url'], data['recipes'][i]['publisher'], data['recipes'][i]['publisher_url']])
        return recipes