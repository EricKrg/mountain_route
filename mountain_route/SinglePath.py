
class SinglePath(object):
    def __init__(self, list_of_points):
        self.path = list_of_points
        self.sum = self.path_sum()

    def path_sum(self):
        path_sum = 0 
        for pos in self.path:
            path_sum = path_sum + pos.value
        return path_sum
    def cumsum_path(self):
        pass
    def __len__(self):
        return len(self.path)
    

