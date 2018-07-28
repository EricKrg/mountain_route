import pandas as pd
import matplotlib.pyplot as plt


terrain = []
with open('./data/Jena.txt') as file:
    for line in file:
        terrain.append([int(x) for x in line.split()])

pd_terrain = pd.DataFrame(terrain).as_matrix()

print terrain
print pd_terrain

for line in pd_terrain:
    for cell in line:
        print cell


print type(pd_terrain)
# Plot the grid
#plt.imshow(pd_terrain)
#plt.gray()
#plt.show()

