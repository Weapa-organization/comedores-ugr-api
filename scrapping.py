import pandas as pd
import requests
import json

class FoodStructure:
    name: str
    allergens: list
    type: str

    def __init__(self, name, allergens, type):
        self.name = name
        self.allergens = allergens
        self.type = type

    def __str__(self):
        return f"name : {self.name}, allergens : {self.allergens}"

    def render_json(self):
        return {
            "nombre": self.name,
            "alergenos": self.allergens
        }

class MenuModel:
    starter: FoodStructure
    main: FoodStructure
    extra: FoodStructure
    dessert: FoodStructure
    date: str

    def __init__(self, starter, main, extra, dessert, date):
        self.starter = starter
        self.main = main
        self.extra = extra
        self.dessert = dessert
        self.date = date

def calculate_date(date):
    month_parse = {
        'ENERO': '01',
        'FEBRERO': '02',
        'MARZO': '03',
        'ABRIL': '04',
        'MAYO': '05',
        'JUNIO': '06',
        'JULIO': '07',
        'AGOSTO': '08',
        'SEPTIEMBRE': '09',
        'OCTUBRE': '10',
        'NOVIEMBRE': '11',
        'DICIEMBRE': '12'
    }

    date = date.split(' ')
    day = date[1]
    month = date[3]
    year = date[5]

    # Parsear month
    month = month_parse[month]

    return f'{year}-{month}-{day}'

def parse_menu(food, allergies, type):

    name = food
    allergens = ''
    if str(allergies) != 'nan':
        allergens = str(allergies)

    return FoodStructure(name, allergens, type)



# Read data from website
df = pd.read_html('https://scu.ugr.es/pages/menu/comedor')

# Column 0 Type, Column 1 Food and Column 2 Allergens
menu_fuentenueva = df[0]
menu_pts = df[1]

menus_fuentenueva = []

types = menu_fuentenueva[0]
foods = menu_fuentenueva[1]
allergies = menu_fuentenueva[2]

date = ''

for index, food in enumerate(foods):
    if food == 'Menú 1' or food == 'Menú 2':
        if food == 'Menú 1':
            date = calculate_date(foods[index-1])
        starter = parse_menu(foods[index+1], allergies[index+1], 'starter')
        main = parse_menu(foods[index+2], allergies[index+2], 'main')
        extra = FoodStructure('', '', 'extra')
        dessert = FoodStructure('', '', 'dessert')
        if types[index+3] == 'Acompañamiento':
            extra = parse_menu(foods[index+3], allergies[index+3], 'extra')
            dessert = parse_menu(foods[index+4], allergies[index+4], 'dessert')
        elif types[index+3] == 'Postre':
            dessert = parse_menu(foods[index+3], allergies[index+3], 'dessert')

        menus_fuentenueva.append(MenuModel(starter, main, extra, dessert, date))

url = 'http://localhost:8000/api/v1/menus'

for menu in menus_fuentenueva:

    payload = {
        'entrante': menu.starter.render_json(),
        'principal': menu.main.render_json(),
        'acompaniamiento': menu.extra.render_json(),
        'postre': menu.dessert.render_json(),
        'date': menu.date
    }

    print(payload)

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

