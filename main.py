import mountain_route


jena = mountain_route.Terrain("./data/jena.txt")
jena.read_terrain()
jena.show_rare()
#jena.show_terrain()
jena.show_interactive()


#paths = mountain_route.PathCollection(jena.terrain)
