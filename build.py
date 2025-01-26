#!/usr/bin/env python
import yaml
import markdown
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("build"),
    autoescape=select_autoescape()
)

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
        for ingredient in bev[name]['ingredients']:
            print(f'<li>{ingredient[list(ingredient)[0]]} {list(ingredient)[0]}</li>')
        print(markdown.markdown(bev[name]['directions']))

for ingredient in menu['out_of_stock']:
    print(ingredient)
