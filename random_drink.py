import requests

# initial ingredient search and response
# ingredient_lookup = input("Search by ingredient:  ")
response = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/random.php')

# filtering of the first drink
cocktails = response.json()['drinks'][0]

# making filtering more readable
drink_id = cocktails["idDrink"]
drink_name = cocktails["strDrink"]
category = cocktails["strCategory"]
glass_type = cocktails["strGlass"]
alcoholic = cocktails["strAlcoholic"]
alcoholic_state = "No"
instructions = cocktails["strInstructions"]
if alcoholic == "Alcoholic":
    alcoholic = "Yes"
else:
    alcoholic = "No"

print(f"""
Drink DB ID: {drink_id}
Drink Name: {drink_name}
Category: {category}
Glass Type: {glass_type}
Alcoholic: {alcoholic}
Instructions: {instructions}
""")
