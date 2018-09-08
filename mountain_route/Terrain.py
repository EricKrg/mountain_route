import pandas as pd
import plotly.graph_objs as go
import mountain_route as mr

# -----
class Terrain(object):
    def __init__(self, con):
        if con != False: # that way i can create an empty obj.
            self.con = con
            self.terrain = self.read_terrain()

    def read_terrain(self):
        terrain = []
        with open(self.con, "r") as file_terrain:
            for line in file_terrain:
                terrain.append([int(x) for x in line.split()])
        #self.terrain = pd.DataFrame(terrain).values
        return pd.DataFrame(terrain).values # terrain
    def get_track(self):
        if len(self.terrain) == 0:
            raise EmptyTerrainError("no terrain data, did  you call Terrain.read_terrain()?")
        else:
            collection = mr.PathCollection()   # collection obj. with all paths
            path = []   #  list of positions obj.
            #print("Nr. of routes: {}".format(range(len(self.terrain) - 1)))
            for line in range(len(self.terrain)):
                search = True
                posi = mr.Pos((line, 0), self.terrain[line][0])  # init y + x
                path.append(posi)
                while search:
                    # each step is stored as dict, the height value corresponds to the xy coord
                    if posi.y == 0:
                        steps = {posi.straigth(self.terrain): (posi.y, posi.x + 1)} #  dict. to add a specific value to a pos.
                        steps[posi.down(self.terrain)] = (posi.y + 1, posi.x + 1)

                        min_p = steps[min(steps.keys())]
                        posi = (mr.Pos(min_p, self.terrain[min_p[0], min_p[1]]))

                        path.append(posi)

                    elif posi.y == len(self.terrain) - 1:
                        steps = {posi.straigth(self.terrain): (posi.y, posi.x + 1)}
                        steps[posi.up(self.terrain)] = (posi.y - 1, posi.x + 1)

                        min_p = steps[min(steps.keys())]
                        posi = (mr.Pos(min_p, self.terrain[min_p[0], min_p[1]]))

                        path.append(posi)

                    else:
                        steps = {posi.straigth(self.terrain): (posi.y, posi.x + 1)}
                        steps[posi.down(self.terrain)] = (posi.y + 1, posi.x + 1)
                        steps[posi.up(self.terrain)] = (posi.y - 1, posi.x + 1)

                        min_p = steps[min(steps.keys())]
                        posi = (mr.Pos(min_p, self.terrain[min_p[0], min_p[1]]))

                        path.append(posi)

                    if posi.x == len(self.terrain[1])-1: # runner is at the end
                        search = False

                collection.add(mr.SinglePath(path))
                path = []
                steps = None
            return collection
    def get_lowest(self):
        #value = self.terrain.min() # actual lowest position
        positions = []
        for col in range(len(self.terrain[0])):
            values = dict()
            for line in range(0,len(self.terrain)):
                values[self.terrain[line][col]] = line
            positions.append(mr.Pos((values[min(values)],col),min(values)))
        return positions
    def geo_ref(self):
        #  to do:
        #  add support for georeferenced rasters
        pass

    # simple show functions
    def show_rare(self):
        print(self.terrain)

    def show_interactive(self):
        data = go.Heatmap(z= self.terrain,
                          colorscale='Greys')
        return data
        #pyo.plot(data)


class EmptyTerrainError(Exception):
    pass