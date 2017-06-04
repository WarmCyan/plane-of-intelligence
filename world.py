

class GridSquare:
   
    def __init__(self, x, y):
        self.x = x
        self.y = y


class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.grid = [][]

        self.g_ais = []

    def initalizeGrid(self):
        print("Initalizing grid of size " + str(width) + "x" + str(height))
        for y in range(0, self.height):
            for x in range(0, self.width):
                grid[x][y] = GridCell(x+y, x,y)
	
	

    # input structure: ('|' delimited ais, ','  delimited modules, ' ' delimited values
    # ",,0 0 1 3 4 5,2 1 7...|[next ai]"
    def world_tick(self, aiinputstring):
        
        # run through every ai input
        aiinputs = aiinputstring.split("|")
        for ai_index in range(0, len(aiinputs)):
            aiinput = aiinputs[ai_index]
            ai = self.g_ais[ai_index]
            
            # verify ai input moves (make sure that number of outputs matches available
            # ai modules
            modules = aiinput.split(",")
            for module_index in range(0, len(modules)):
                module_vals = modules[module_index]
                module = ai.modules[module_index]

                if not module.allowsOutput and len(module_vals) > 0:
                    print("WARNING - AI attempting to output on non-output module")
                    continue
                
                values = module_vals.split(" ")
                module.runOutput(self, values)
                # handle values in module
        
        # handle world update (energy, etc.)

        # create input sets
        inputstrings = ""
        for ai in g_ais:
            inputstring = ""
            for module in ai.modules:
                inputstring += module.runInput(self) + ","
            inputstring = inputstring[:-1]
            
            inputstrings += inputstring + "|"

        inputstrings = [:-1]
        return inputstrings
            

class GridCell:
	def __init__(self, energy, x, y):
		self.energy = energy
		self.pos = [x,y]
		self.energyShift = [0,0,0,0,0,0,0,0] #center right, upper right, upper center, upper left, center left, lower left, lower center, lower right
	
	def calcEnergyShift(self, grid):
		if(self.pos[0] != 0 and self.pos[0] < len(grid) and self.pos[1] != 0 and self.pos[1] < len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[1] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+1])
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
			self.energyShift[3] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+1])
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
			self.energyShift[5] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]-1])
			self.energyShift[6] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
			self.energyShift[7] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]-1])
		if(self.pos[0] == 0 and self.pos[0] < len(grid) and self.pos[1] != 0 and self.pos[1] < len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[1] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+1])
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
			self.energyShift[3] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
			self.energyShift[7] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]-1])
		if(self.pos[0] == 0 and self.pos[0] < len(grid) and self.pos[1] == 0 and self.pos[1] < len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[1] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+1])
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
		if(self.pos[0] == 0 and self.pos[0] < len(grid) and self.pos[1] != 0 and self.pos[1] >= len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[6] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
			self.energyShift[7] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]-1])
		if(self.pos[0] != 0 and self.pos[0] < len(grid) and self.pos[1] == 0 and self.pos[1] < len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[1] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+1])
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
			self.energyShift[3] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+1])
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
		if(self.pos[0] != 0 and self.pos[0] >= len(grid) and self.pos[1] == 0 and self.pos[1] < len(grid[0])):
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
			self.energyShift[3] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+1])
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
		if(self.pos[0] != 0 and self.pos[0] < len(grid) and self.pos[1] != 0 and self.pos[1] >= len(grid[0])):
			self.energyShift[0] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]+0])
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
			self.energyShift[5] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]-1])
			self.energyShift[6] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
			self.energyShift[7] = self.calcSingleEnergyShift(grid[self.pos[0]+1][self.pos[1]-1])
		if(self.pos[0] != 0 and self.pos[0] >= len(grid) and self.pos[1] != 0 and self.pos[1] >= len(grid[0])):
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
			self.energyShift[5] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]-1])
			self.energyShift[6] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
		if(self.pos[0] != 0 and self.pos[0] >= len(grid) and self.pos[1] != 0 and self.pos[1] < len(grid[0])):
			self.energyShift[2] = self.calcSingleEnergyShift(grid[self.pos[0]+0][self.pos[1]+1])
			self.energyShift[3] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+1])
			self.energyShift[4] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]+0])
			self.energyShift[5] = self.calcSingleEnergyShift(grid[self.pos[0]-1][self.pos[1]-1])
			self.energyShift[6] = self.calcSingleEnergyShift(grid[self.pos[0]-0][self.pos[1]-1])
	
	def calcSingleEnergyShift(self, cell):
		if(cell.energy >= self.energy):
			return 0
		return (self.energy - en) / 2
	
	def executeEnergyShift(self, grid):
		if(self.energyShift[0] != 0):
			grid[self.pos[0]+1][self.pos[1]+0].energy += self.energyShift[0]
		if(self.energyShift[1] != 0):
			grid[self.pos[0]+1][self.pos[1]+1].energy += self.energyShift[1]
		if(self.energyShift[2] != 0):
			grid[self.pos[0]+0][self.pos[1]+1].energy += self.energyShift[2]
		if(self.energyShift[3] != 0):
			grid[self.pos[0]-1][self.pos[1]+1].energy += self.energyShift[3]
		if(self.energyShift[4] != 0):
			grid[self.pos[0]-1][self.pos[1]+0].energy += self.energyShift[4]
		if(self.energyShift[5] != 0):
			grid[self.pos[0]-1][self.pos[1]-1].energy += self.energyShift[5]
		if(self.energyShift[6] != 0):
			grid[self.pos[0]+0][self.pos[1]-1].energy += self.energyShift[6]
		if(self.energyShift[7] != 0):
			grid[self.pos[0]+1][self.pos[1]-1].energy += self.energyShift[7]
		
