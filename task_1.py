import requests

# ask user for ingredient and make the request
requested_ingredient = input("Search by ingredient:  ")
ingredient_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={requested_ingredient}')

# Make a list of the returned json
cocktails = ingredient_lookup.json()['drinks']

# make an empty list to be populated with formatted data later
filtered_cocktails = []

# loop over the json and extract the formatted names into the list that was just prepared
for i in cocktails:
    filtered_cocktails.append(i['strDrink'])

# Print each member of the formatted list individually
for x in filtered_cocktails:
    print(x)
