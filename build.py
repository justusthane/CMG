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

print(menu)

for bev, details in menu['menu'].items():
    #print(bev)
    print(bev)
    for ingredient in details['ingredients']:
        print(f'<li>{ingredient[list(ingredient)[0]]} {list(ingredient)[0]}</li>')
    print(markdown.markdown(details['directions']))
    details['directions_html'] = markdown.markdown(details['directions'])

with open('index.html', 'w') as file:
    file.write(templateMenu.render(bevs = menu['menu']))

with open('recipes.html', 'w') as file:
    file.write(templateRecipes.render(bevs = menu['menu']))

for ingredient in menu['out_of_stock']:
    print(ingredient)
