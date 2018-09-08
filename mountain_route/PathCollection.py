
class PathCollection(object):
    def __init__(self):
        self.paths = []

    def __len__(self):
        return len(self.paths) # number of paths stored

    def add(self, path):
        self.paths.append(path)

    def best_path(self):
        temp_dict = {path.sum:path for path in self.paths}
        return temp_dict[min(temp_dict)] # choose the path with the over all min. sum

    # this needs to be done, because if i would process all path (i.e. for an 480 by 800 cell big raster), the loading time to display all would take too long
    def all_path_array(self):
        x = []
        y = []
        z = []
        for path in self.paths:
            for pos in path.path:
                x.append(pos.x)
                y.append(pos.y)
                z.append(1000)
        data = [x,y,z]
        return data