import requests
import json

YummlyAPI_appID = "4219c174"
YummlyAPI_appKEY = "6de0076d510d794329a6b2157302912a"

YummlyAPI_maxReslts = "&maxResult=100&start=100"

Yummly_URL = "http://api.yummly.com/v1/api/recipes?_app_id="+YummlyAPI_appID+"&_app_key="+YummlyAPI_appKEY+"&allowedCuisine[]=cuisine^cuisine-"

cuisines_list = [
                 'American', 'Italian', 'Asian', 'Mexican',
                 'Southern & Soul Food', 'French', 'Southwestern', 'Barbecue',
                 'Indian', 'Chinese', 'Cajun & Creole', 'English', 'Mediterranean',
                 'Greek', 'Spanish', 'German', 'Thai', 'Moroccan', 'Irish', 'Japanese',
                 'Cuban', 'Hawaiin', 'Swedish', 'Hungarian', 'Portugese'
                ]

IDs = []

for cuisine in cuisines_list:
    res = requests.get(Yummly_URL+cuisine+YummlyAPI_maxReslts)
    json = res.json()

    for recipe in json['matches']:
        recipe_id = recipe.id
        print(recipe_id)