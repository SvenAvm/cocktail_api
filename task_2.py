import requests

# ask user for ingredient and make the request
requested_ingredient = input("Search by ingredient:  ")
ingredient_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={requested_ingredient}')

# filtering of the first drink
cocktails = ingredient_lookup.json()['drinks'][0]

# defining keywords to lookup in json
name = cocktails["strDrink"]
drink_id = cocktails["idDrink"]

# second lookup to get all data for the requested drink
id_lookup = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}")

full_cocktail = id_lookup.json()['drinks'][0]

glass = full_cocktail["strGlass"]
alcoholic = full_cocktail["strAlcoholic"]
alcoholic_state = "No"
instructions = full_cocktail["strInstructions"]
if alcoholic == "Alcoholic":
    alcoholic = "Yes"
else:
    alcoholic = "No"

print(f"""
Name: {name}
Glass: {glass}
Alcoholic: {alcoholic}
Instructions: {instructions}
""")
