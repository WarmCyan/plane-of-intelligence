import world


w = world.World(100, 100)
w.initalizeGrid()

def progressBar(current,max):
    print("\r",end="")
    s = "["
    for i in range(0,int((current/max)*20)):
        s += "="
    s += ">"
    print(s,end="")

print("[                    ]",end="")
for i in range(0, 240):
    #w.printGrid()
    w.runEnergyFlow()
    w.writeImage(i)
    progressBar(i,240)
    #input()
