#!/usr/bin/env python
import yaml

def writeLine(string):
    global menuOut
    menuOut += f"{string}\r\n"

with open('menu.yaml', 'r') as file:
    menu = yaml.safe_load(file)


#print(menu['menu'])

menuOut = '''\
<html>
<head>
<link rel="stylesheet" href="style.css">
<title>Cocktail Menu</title>
</head>
<body>
'''

for bev in menu['menu']:
    #print(bev)
    for name in bev:
        print(name)
        writeLine(f'<h2>{name}</h2>')
        writeLine('<ul>')
        for ingredient in bev[name]['ingredients']:
            writeLine(f'<li>{ingredient}</li>')
        writeLine('</ul>')

menuOut += '''\
</body>
</html>
'''

with open('index.html', 'w') as file:
    file.write(menuOut)
