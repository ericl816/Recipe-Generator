
import requests, sys, bs4, json

def scrapeRecipes(listOfFoods):
    print('web scrape function called')

    API_Key = 'b156004663932aa132f0188da4715558'
    ingredients = ",".join(listOfFoods)
    
    searchRequestURL = "https://www.food2fork.com/api/search?key={0}&q={1}".format(API_Key,ingredients)
    searchRes = requests.get(searchRequestURL)

    #obtain search response, returns a bunch of recipe ids
    searchResultsDic = json.loads(searchRes.text)
    #acquire each recipe details by id 
    tmp = 1
    for r in searchResultsDic['recipes']:
        if(tmp >2):
            break
        tmp+=1
        recipeID = r['recipe_id']
        recipeRequestURL = "https://www.food2fork.com/api/get?key={0}&rId={1}".format(API_Key,recipeID)
        recipeRes = requests.get(recipeRequestURL)
        # recipeDic: 
        # 	image_url: URL of the image
        # 	source_url: Original Url of the recipe on the publisher's site
        # 	f2f_url: Url of the recipe on Food2Fork.com
        # 	title: Title of the recipe
        # 	publisher: Name of the Publisher
        # 	publisher_url: Base url of the publisher
        # 	social_rank: The Social Ranking of the Recipe (As determined by our Ranking Algorithm)
        # 	ingredients: The ingredients of this recipe
        recipeDic = json.loads(recipeRes.text)
        print(recipeDic)


    



