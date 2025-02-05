#!/usr/bin/env python
import yaml
import markdown
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader("build"),
    autoescape=select_autoescape()
)

def generateMenu():
    with open('menu/menu.yaml', 'r') as file:
        menu = yaml.safe_load(file)

    templateMenu = env.get_template("menu.html")
    templateRecipes = env.get_template("recipes.html")

    for bev, details in menu['menu'].items():
        #print(bev)
        print(bev)
        #for ingredient in details['ingredients']:
        #    print(f'<li>{ingredient[list(ingredient)[0]]} {list(ingredient)[0]}</li>')
        details['directions_html'] = markdown.markdown(details['directions'])

    menuHtml = templateMenu.render(bevs = menu['menu'])
    recipesHtml = templateRecipes.render(bevs = menu['menu'])
    return {'menuHtml': menuHtml, 'recipesHtml': recipesHtml}

if (__name__ == 'build'):
    from flask import Flask

    app = Flask(__name__)
        
    @app.route("/")
    def serveMenu():
        return generateMenu()['menuHtml']
    @app.route("/recipes")
    def serveRecipes():
        return generateMenu()['recipesHtml']

elif (__name__ == '__main__'):
    html = generateMenu()
    with open('index.html', 'w') as file:
        file.write(html['menuHtml'])

    with open('recipes.html', 'w') as file:
        file.write(html['recipesHtml'])


print(generateMenu())
#print(menu)
#
#
#
#for ingredient in menu['out_of_stock']:
#    print(ingredient)
#
#print(__name__)
