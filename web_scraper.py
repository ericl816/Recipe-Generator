import requests, sys, bs4, os, json
API_KEY = 'e3c679808020ba0a3aa594c8a2300160'

def scrape(listOfFoods):
    print('web scrape function called')
    listOfFoods.append('recipes')
    """for i in listOfFoods:
        print(i)"""
    myRequestURL = 'https://google.com/search?q='+" ".join(listOfFoods)
    print(myRequestURL)
    res = requests.get(myRequestURL)
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    headlineResults = soup.find_all('a')

    for h in headlineResults:
        print(h)

class Scraper:
    def __init__(self, listOfFoods, num_recipes):
        ingredients = ','.join(listOfFoods)
        self.num = num_recipes
        self.url = 'https://www.food2fork.com/api/search?key={0}&q={1}&sort=r'.format(API_KEY, ingredients)
        print(self.url)

    def scrape (self):
        print('calling API...')
        # E.g.: https://www.food2fork.com/api/search?key=e3c679808020ba0a3aa594c8a2300160&q=Eggs
        response = requests.get(self.url)
        data = json.loads(response.text)
        recipes = []
        self.num = min(self.num, data['count']) # Limited to only 50 calls per day
        # Return title, social ranking, image url, and source_url for each recipe
        for i in range(self.num):
            recipes.append([data['recipes'][i]['title'], str(data['recipes'][i]['social_rank']), data['recipes'][i]['image_url'], data['recipes'][i]['source_url']])
        return recipes
