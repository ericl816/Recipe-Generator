# Recipe Generator

A web app that takes in a list of foods from user provided input, scrapes the web with that data, parses the results, and then feeds it into a machine learning model to give the user the best meals and recipes!

### Project Hierarchy
Web App
- List of Foods Available (Input)
- Recipe Results (Output)
    - Recipe Ratings (Our machine learning model assigns a score to each recipe)
    - Safety Warning (Some mixed foods in the recipes don't go well)

Back-End (Flask)
- Web Scraping (Food2Fork API)
- Parsing (BeautifulSoup)
- ML Model
