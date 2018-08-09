from mountain_route import Pos,PathCollection,Terrain
import pandas as pd
import plotly.offline as pyo
import  plotly.graph_objs as go

'''
jena = Terrain("./data/jena.txt")
jena.read_terrain()
jena.show_rare()


jena_collection = jena.get_track()

df = pd.DataFrame(columns=["x", "y","value"])

for track in jena_collection.paths[2]:
    df = df.append({
        "x": track.x,
        "y": track.y,
        'value': track.value
    }, ignore_index=True)

print(df)
path = go.Heatmap(x=df['x'],
                  y=df['y'],
                  z=df['value'],
                  colorscale = [
                      [0, 'rgb(180, 0, 0)'],
                      [1, 'rgb(180, 0, 0)']
                  ],
                  showscale=False)
terrain = jena.show_interactive()

data = [terrain, path]
pyo.plot(data)
#jena.show_terrain()
'''

colorado = Terrain("./data/Colorado_844x480.txt")
colorado.read_terrain()
colorado.show_rare()


colorado_collection = colorado.get_track()

df = pd.DataFrame(columns=["x", "y","value"])

for track in colorado_collection.paths[2]:
    df = df.append({
        "x": track.x,
        "y": track.y,
        'value': track.value
    }, ignore_index=True)

#print(df)
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