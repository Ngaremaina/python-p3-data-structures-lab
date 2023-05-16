spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [names.get("name") for names in spicy_foods]
    
def get_spiciest_foods(spicy_foods):
    return [spicy for spicy in spicy_foods if spicy.get('heat_level') > 5]
     
def print_spicy_foods(spicy_foods):
    for foods in spicy_foods:
        names = foods.get('name')
        cuisine = foods.get('cuisine')
        heat_level = "\U0001F336" * foods.get('heat_level')
        print(f"{names} ({cuisine}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for foods in spicy_foods:
        if foods.get('cuisine') == cuisine:
            return foods
        
def print_spiciest_foods(spicy_foods):
    for foods in spicy_foods:
        if foods.get('heat_level') > 5:
            names = foods.get('name')
            cuisine = foods.get('cuisine')
            heat_level = "\U0001F336" * foods.get('heat_level')
            print(f"{names} ({cuisine}) | Heat Level: {heat_level}")

def get_average_heat_level(spicy_foods):
    sum = 0
    for foods in spicy_foods:
        sum += foods.get('heat_level')
    return sum / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
    

