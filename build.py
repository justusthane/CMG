#!/usr/bin/env python
import yaml
import markdown
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("build"),
    autoescape=select_autoescape()
)
menuOut = ''
recipesOut = ''

def writeMenu(string):
    global menuOut
    menuOut += f"{string}\r\n"

def writeRec(string):
    global recipesOut
    recipesOut += f"{string}\r\n"

with open('menu.yaml', 'r') as file:
    menu = yaml.safe_load(file)

templateMenu = env.get_template("menu.html")
templateRecipes = env.get_template("recipes.html")

with open('index.html', 'w') as file:
    file.write(templateMenu.render(bevs = menu['menu']))

with open('recipes.html', 'w') as file:
    file.write(templateRecipes.render(bevs = menu['menu']))

print(menu['menu'])

for bev in menu['menu']:
    #print(bev)
    for name in bev:
        print(name)
        writeMenu(f'<h2>{name}</h2>')
        writeRec(f'<h2>{name}</h2>')
        writeMenu('<ul>')
        writeRec('<ul>')
        for ingredient in bev[name]['ingredients']:
            writeMenu(f'<li>{list(ingredient)[0]}</li>')
            writeRec(f'<li>{ingredient[list(ingredient)[0]]} {list(ingredient)[0]}</li>')
        writeMenu('</ul>')
        writeRec('</ul>')
        writeRec('<h3>Directions</h3>')
        writeRec(markdown.markdown(bev[name]['directions']))

for ingredient in menu['out_of_stock']:
    print(ingredient)



testDict = {
        'First item': {'nest': 'dict'},
        'Second item': 'Bywe',
        'Third item': 'Okay'
        }

print(testDict)

for k, v in testDict.items():
    print(f"{k}: {v}")
