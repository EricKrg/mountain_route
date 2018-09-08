import  plotly.graph_objs as go

# display class with to display function, i created this one to keep the app.py a bit cleaner
class Display(object):
    def __init__(self, obj_list):
        self.obj_list = obj_list # list of pos obj.
        self.df = []
    def to_display(self,col, graph):
        x = []
        y = []
        z = []
        for obj in self.obj_list:
            x.append(obj.x)
            y.append(obj.y)
            z.append(obj.value)
        self.df = [x, y, z]

        if graph == 'heat':
            data = self.heatmap(col)
        elif graph == 'line':
            data = self.line(col)
        elif graph == 'histo':
            data = self.histo(col)
        return data

    def heatmap(self,col):
        color = ['rgb(180, 0, 180)', 'rgb(250, 100, 250)', 'rgb(180, 0, 0)']
        if col == 999: scale = 'Hot'; show = False #True, atm there is a problem with mutliple scales
        else: scale = [[0, color[col]],[1, color[col]]];show = False
        data = go.Heatmap(x=self.df[0],
                   y=self.df[1],
                   z=self.df[2],
                   colorscale=scale, showscale=show)
        return data

    def line(self,col):
        data = go.Scatter3d(x=[i for i in range(len(self.obj_list))], # number of pos in obj_list
                          y = self.df[1],
                          z=self.df[2],
                          mode = 'lines',
                          )
        return data
    def histo(self,col):
        data = go.Histogram(
            x = self.df[2]
        )
        return data