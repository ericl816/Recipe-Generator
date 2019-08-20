import requests, sys, bs4

def scrape(listOfFoods):
    print('web scrape function called')
    listOfFoods.append('recipes')
    myRequestURL = 'https://google.com/search?q='+" ".join(listOfFoods)
    print(myRequestURL)
    res = requests.get(myRequestURL)
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    headlineResults = soup.find_all('a')

    for h in headlineResults:
        print(h)