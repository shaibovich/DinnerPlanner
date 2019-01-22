import requests
import json

YummlyAPI_appID = "4219c174"
YummlyAPI_appKEY = "6de0076d510d794329a6b2157302912a"

YummlyAPI_maxReslts = "&maxResult=100&start=100"

Yummly_URL = "http://api.yummly.com/v1/api/recipes?_app_id=" + YummlyAPI_appID + "&_app_key=" + YummlyAPI_appKEY + "&allowedCuisine[]=cuisine^cuisine-"

Yummly_recipe_url = "http://api.yummly.com/v1/api/recipe/{id}?_app_id=" + YummlyAPI_appID + "&_app_key=" + YummlyAPI_appKEY

'http://api.yummly.com/v1/api/recipes?_app_id=4219c174&_app_key=6de0076d510d794329a6b2157302912a&q=onion+soup'
'http://api.yummly.com/v1/api/recipe/Classic-French-Onion-Soup-2631541?_app_id=4219c174&_app_key=6de0076d510d794329a6b2157302912a'

cuisines_list = [
    'American', 'Italian', 'Asian', 'Mexican',
    'Southern & Soul Food', 'French', 'Southwestern', 'Barbecue',
    'Indian', 'Chinese', 'Cajun & Creole', 'English', 'Mediterranean',
    'Greek', 'Spanish', 'German', 'Thai', 'Moroccan', 'Irish', 'Japanese',
    'Cuban', 'Hawaiin', 'Swedish', 'Hungarian', 'Portugese'
]

IDs = []

def convert_to_add_dish_obj(recipe):
    obj = {
        'name': recipe['name'],
        'photoLink': get_phoot_link(recipe['images']),
        'calories': get_recipe_calories(recipe['nutritionEstimates']),
        'peopleCount': recipe['numberOfServings'],
        'ingredients': get_ingredient_list(recipe['ingredientLines']),
        'recipe': get_recipe_text(recipe['source']['sourceRecipeUrl']),
        'cookingTime': recipe['totalTime']
    }
    return obj


def get_recipe_text(recipe_link):
    result = requests.get(recipe_link).text
    sub_result = result[result.find('recipeInstructions'):]
    sub_result = sub_result[:sub_result.find("\n")]
    print(sub_result)
    return sub_result



def get_ingredient_list(ing_list):
    lst = []
    for ing in ing_list:
        lst.append({
            'name': ing,
            'count': 1
        })
    return lst


def get_phoot_link(images):
    for img in images:
        if 'hostedLargeUrl' in img:
            return img['hostedLargeUrl']
    for img in images:
        if 'hostedMediumUrl' in img:
            return img['hostedMediumUrl']
    for img in images:
        if 'hostedSmallUrl' in img:
            return img['hostedSmallUrl']
    return ""


def get_recipe_calories(nut_list):
    for nut in nut_list:
        if 'attribute' in nut and nut['attribute'] == 'FAT_KCAL' and 'value' in nut:
            return nut['value']
    return 0


for cuisine in cuisines_list:
    lst = []
    res = requests.get(Yummly_URL + cuisine + YummlyAPI_maxReslts)
    json = res.json()

    for recipe in json['matches']:
        recipe_id = recipe['id']
        recipe_res = requests.get(Yummly_recipe_url.format(id=recipe_id)).json()
        lst.append(convert_to_add_dish_obj(recipe_res))

    print(lst)



