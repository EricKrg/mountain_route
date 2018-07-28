from mountain_route import Pos,PathCollection,Terrain

jena = Terrain("./data/jena.txt")
jena.read_terrain()
jena.show_rare()
#jena.show_terrain()



path = []
# main greedy algo --> should be added to searcher class
for line in range(len(jena.terrain)-1):
    print("line {}".format(line))
    search = True
    posi = Pos((line, 0), jena.terrain[line][0]) # init y + x
    path.append(posi)
    while search:
        if posi.y == 0:
            steps = { posi.straigth(jena. terrain) : (posi.y, posi.x + 1) }
            steps[posi.down(jena.terrain)] = (posi.y + 1, posi.x+1)

            min_p = steps[min(steps.keys())]
            posi = (Pos(min_p, jena.terrain[min_p[0], min_p[1]]))

            path.append(posi)
            print(posi.show())
        elif posi.y == len(jena.terrain):
            steps = {posi.straigth(jena.terrain): (posi.y, posi.x + 1)}
            steps[posi.up(jena.terrain)] = (posi.y - 1, posi.x + 1)

            min_p = steps[min(steps.keys())]
            posi = (Pos(min_p, jena.terrain[min_p[0], min_p[1]]))

            path.append(posi)
            print(posi.show())
        else:
            steps = {posi.straigth(jena.terrain): (posi.y, posi.x + 1)}
            steps[posi.down(jena.terrain)] = (posi.y + 1, posi.x + 1)
            steps[posi.up(jena.terrain)] = (posi.y - 1, posi.x + 1)

            min_p = steps[min(steps.keys())]
            posi = (Pos(min_p, jena.terrain[min_p[0], min_p[1]]))

            path.append(posi)
            print(posi.show())

        if posi.x == len(jena.terrain[1])-1: # runner is at the end
            search = False
    #break
    # here add path to PathCollection
    path = []


#paths = mountain_route.PathCollection(jena.terrain)
