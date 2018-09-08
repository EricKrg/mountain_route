from mountain_route import Pos,PathCollection,Terrain, Display
import pandas as pd
import plotly.offline as pyo
import  plotly.graph_objs as go

'''
jena = Terrain("./data/jena.txt")
#
low_pos = jena.get_lowest()
tracks = jena.get_track()
best_track = tracks.best_path().path
all_tracks = tracks.all_path_array() # way to display all paths

data = []
data.append(jena.show_interactive())

all = Display([]) # create an empty Display obj
all.df = all_tracks # fill it with the prepared all_tracks arrays
data.append(all.heatmap(2))

i = 0
for obj in [low_pos,best_track]:
    data.append(Display(obj).to_display(col = i))
    i += 1

pyo.plot(data) # this plot shows the whole thing upside down
'''
colorado = Terrain('./data/Colorado_844x480.txt')

low_pos = colorado.get_lowest()
tracks = colorado.get_track() # get routing for all tracks
best_track = tracks.best_path().path # extract the best path
all_tracks = tracks.all_path_array() # way to display all paths

data = []
data.append(colorado.show_interactive()) # show the background elevation

all = Display([]) # create an empty Display obj
all.df = all_tracks # fill it with the prepared all_tracks arrays
data.append(all.heatmap(2))

i = 0
for obj in [low_pos,best_track]:
    data.append(Display(obj).to_display(col = i)) # create display obj. for best path and low areas
    i += 1

pyo.plot(data) # this plot shows the whole thing upside down




'''

colorado = Terrain('./data/Colorado_844x480.txt')
colorado.show_rare()

colorado_collection = colorado.get_track()

df = pd.DataFrame(columns=["x", "y","value"])

for track in colorado_collection.paths[2]:
    df = df.append({
        "x": track.x,
        "y": track.y,
        'value': track.value
    }, ignore_index=True)


path = go.Heatmap(x=df['x'],
                  y=df['y'],
                  z=df['value'],
                  colorscale = [
                      [0, 'rgb(180, 0, 0)'],
                      [1, 'rgb(180, 0, 0)']
                  ],
                  showscale=False)
terrain = colorado.show_interactive()

data = [terrain, path]
pyo.plot(data)
'''