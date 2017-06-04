import world


w = world.World(10, 10)
w.initalizeGrid()

for i in range(0, 240):
    #w.printGrid()
    w.runEnergyFlow()
    w.writeImage(i)
    #input()
