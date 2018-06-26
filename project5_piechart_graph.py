import pygal

pets = []
petsCount = {}

file = open('project5_pets.txt')
pets = file.read().splitlines()
piechart = pygal.Pie()
piechart.title = "Favourite Pets"

barchart = pygal.Bar()
barchart.title = "Favourite Pets"

for animal in pets:
    data = animal.split(" ")
    petsCount[data[0]] = data[1]
    piechart.add(data[0], int(data[1]))
    barchart.add(data[0], int(data[1]))


piechart.render_to_file('project5_piechart.svg')
barchart.render_to_file('project5_barchart.svg')

