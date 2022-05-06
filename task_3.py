import requests

# ask user for ingredient, make the request and sort result to list
requested_ingredient = input("Search by ingredient:  ")
ingredient_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=gin')
list_by_ingredients = ingredient_lookup.json()['drinks']
id_by_ingredient = []

# ask user for name, make the request and sort result to list
requested_name = input("Search by Name:  ")
name_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s=martini')
list_by_name = name_lookup.json()['drinks']

# Create Lists to filter the results inside later
search_by_ingredient_names = []
final_cocktails = []

# Filter the initial search with the name parameter
for x in list_by_ingredients:
    search_by_ingredient_names.append(x['strDrink'])
for x in search_by_ingredient_names:
    if requested_name in x:
        final_cocktails.append(x)

# Format the final output
final_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={final_cocktails[0]}')
final_cocktail = final_lookup.json()['drinks'][0]
name = final_cocktail['strDrink']
drink_id = final_cocktail["idDrink"]
glass = final_cocktail["strGlass"]
alcoholic = final_cocktail["strAlcoholic"]
alcoholic_state = "No"
instructions = final_cocktail["strInstructions"]
if alcoholic == "Alcoholic":
    alcoholic = "Yes"
else:
    alcoholic = "No"

# Final Output
print(f"""
Name: {name}
Glass: {glass}
Alcoholic: {alcoholic}
Instructions: {instructions}
""")
