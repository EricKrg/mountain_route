import pandas as pd
import matplotlib.pyplot as plt

# -----

class Terrain(object):
    def __init__(self, con):
        self.con = con
        self.terrain = []

    def read_terrain(self):
        terrain = []
        with open(self.con, "r") as file_terrain:
            for line in file_terrain:
                terrain.append([int(x) for x in line.split()])
        self.terrain = pd.DataFrame(terrain).values

    def geo_ref(self):
        pass

    # simple show functions

    def show_rare(self):
        print(self.terrain)

    def show_terrain(self):
        plt.imshow(self.terrain)
        plt.gray()
        plt.show()
    '''
    def show_interactive(self):
        m = folium.Map(zoom_start=3)
        folium.plugins.ImageOverlay(
            image=self.terrain,
            origin='lower'
        ).add_to(m)

        m.save(outfile="./data/test.html")
    '''