class Module():

    # constructor
    def __init__(self, allowsInput=True, allowsOutput=True):
        self.allowsInput = allowsInput
        self.allowsOutput = allowsOutput
        pass

    def runOutput(self, world, values):
        pass

    # returns correctly delimited values
    def runInput(self, world):
        pass

