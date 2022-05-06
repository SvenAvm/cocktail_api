import requests


ingredient_lookup = requests.get(f'https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Gin')

# filtering of the first drink
cocktails = ingredient_lookup.json()['drinks'][0]

name = cocktails["strDrink"]
drink_id = cocktails["idDrink"]


print(f"""
Name: {name}
""")
