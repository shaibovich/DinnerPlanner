import requests
import json
import re

YummlyAPI_appID = "4219c174"
YummlyAPI_appKEY = "6de0076d510d794329a6b2157302912a"

YummlyAPI_maxReslts = "&maxResult=100&start={start}"

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


def convert_to_add_dish_obj(recipe, ing_lst):
    obj = {
        'name': recipe['name'],
        'photoLink': get_phoot_link(recipe['images']),
        'calories': get_recipe_calories(recipe['nutritionEstimates']),
        'peopleCount': recipe['numberOfServings'],
        'ingredients': get_ingredient_list(recipe['ingredientLines'], ing_lst),
        'recipe': recipe['source']['sourceRecipeUrl'],
        'cookingTime': get_recipe_cooking_time(recipe)
    }
    return obj


def get_recipe_cooking_time(recipe):
    if 'totalTime' not in recipe:
        return 0
    else:
        try:
            return int(recipe['totalTime'].split(' ')[0])
        except Exception:
            return 0



def get_recipe_text(result):
    sub_result = result[result.find('recipeInstructions') + len('recipeInstructions'):]
    sub_result = sub_result[sub_result.find('['):sub_result.find(']')]
    sub_result = sub_result.replace('\r', '')
    sub_result = sub_result.replace('\n', '')
    sub_result = sub_result.replace('\t', '')

    return re.sub('[^A-Za-z0-9 .]+', '', sub_result)


def get_ingredient_list(ing_list, meta_ing_lst):
    lst = []
    for index, ing in enumerate(ing_list):
        if index == len(meta_ing_lst):
            break
        text = ing.split(' ')[0]
        try:
            count = int(text)
        except Exception:
            count = 1
        lst.append({
            'name': meta_ing_lst[index],
            'count': count
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


def check_if_recipe_appear(recipe):
    result = requests.get(recipe['recipe'])
    if result.status_code != 200:
        return None
    if 'recipeInstructions' in result.text:
        recipe['recipe'] = get_recipe_text(result.text)
        return True


def add_to_server(lst):
    requests.post('http://localhost:5050', lst)


for cuisine in cuisines_list:
    for i in range(1,11):
        lst = []
        res = requests.get(Yummly_URL + cuisine + YummlyAPI_maxReslts.format(start=i*100))
        json = res.json()

        for recipe in json['matches']:
            recipe_id = recipe['id']
            recipe_res = requests.get(Yummly_recipe_url.format(id=recipe_id)).json()
            obj = convert_to_add_dish_obj(recipe_res, recipe['ingredients'])
            text_recipe = check_if_recipe_appear(obj)
            if text_recipe is not None:
                lst.append(obj)
        print(json.dumps(lst))

