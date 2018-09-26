import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import  plotly.graph_objs as go

import os
import pandas as pd

import mountain_route as mr
from mountain_route import Display

# app
app = dash.Dash()

# data folder
# i used os to create platform independent paths
dir = os.path.dirname(os.path.abspath(__file__)) # get the home dir
data_dir = os.path.join(dir,'data')
data_list = os.listdir(os.path.join(dir,'data')) # get the data folder
data_dict = [{'label': long, 'value': long} for long in data_list]

# layout 
app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
            id = 'file',
            options= data_dict,
            value='',
            ),
            ],
            style=dict(width='90%', display='table-cell')
        )
        ],
        style = dict(width = '100%', display='table')
    ),

    dcc.RadioItems(id='check',
                  options=[
                      {'label': 'route', 'value': 'r'},
                      {'label': 'all', 'value': 'a'},
                      {'label': 'low areas', 'value': 'l'},
                      {'label': 'no action', 'value': 'n'}
                  ],
                  value='n'
                  ),
    html.Div(id = 'output_main'), # main output depending on radio button input
    html.Div(id='temp', style={'display': 'none'}), # secret data storage
])

def blueprint(id,data, title):
    return dcc.Graph(id=id,figure = {'data':data,'layout':go.Layout(title = title)})


# in case i want to use the  same terrain for multiple actions, i can store it in the undisplayed div called temp

@app.callback(Output('temp', 'children'),
              [Input('file', 'value')])
def terrain_temp(file):
    if file != '':
        new_terrain = mr.Terrain(os.path.join(data_dir,file))
        return pd.DataFrame(new_terrain.terrain).to_json(date_format='iso', orient='split')


@app.callback(Output('output_main', 'children'),
              [Input('file', 'value'),
               Input('check', 'value')])
def route_output(file, check_list):
    data = []
    data2= []
    new_terrain = mr.Terrain(os.path.join(data_dir, file))
    if len(new_terrain.terrain) < 2: html_return = html.Div([html.Div('<b> Sorry Wrong terrain </b>')], style={'allign':'center'})
    else:
        data.append(new_terrain.show_interactive())  # show the background elevation
        if 'r' in check_list:
            tracks = new_terrain.get_track()  # get routing for all tracks
            best_track = tracks.best_path().path
            data2.append(Display(best_track).to_display(graph='line', col=1))
            data.append(Display(best_track).to_display(graph='heat',col=1))

            #check if route goes throug lowest points
            low_list = [i.value for i in new_terrain.get_lowest()]
            track_list = [i.value for i in best_track]
            has_low = False
            for v in track_list:
                if v in low_list:
                    has_low = True
                if has_low: data3 = html.H3('Route goes through low areas')
                else: data3 = html.H3('Route does not go through low areas')
            html_return = html.Div([
                blueprint('1', data, 'Best route'),
                data3,
                blueprint('2', data2, 'Height profile in m'),
            ])

        if 'l' in check_list:
            low_pos = new_terrain.get_lowest()
            data.append(Display(low_pos).to_display(graph='heat',col=999))  # create display obj. for best path and low areas
            data2.append(Display(low_pos).to_display(graph='histo', col=0))
            html_return = html.Div([
                                    blueprint('1', data, 'lowest Areas'),
                                    blueprint('2',data2, 'low Area Distribution')
            ])
        if 'a' in check_list:
            print('all')
            tracks = new_terrain.get_track()  # get routing for all tracks
            all_tracks = tracks.all_path_array()  # way to display all paths

            all = Display([])  # create an empty Display obj
            all.df = all_tracks  # fill it with the prepared all_tracks arrays
            data.append(all.heatmap(2))
            html_return = html.Div([blueprint('1', data, 'All possible routes')])
        if 'n' in check_list:
            data2 = [go.Histogram(x=new_terrain.terrain.ravel(),
                                  opacity=0.75,marker=dict(color='#545659')
                                  )]

            html_return = html.Div([
                                    blueprint('1', data, 'Terrain map'),
                                    blueprint('2', data2, 'Terrain height value distribution')
            ])
    return html_return


# run
if __name__ == '__main__': # if file is called directly, app server is started/run
    app.run_server(debug=True)
