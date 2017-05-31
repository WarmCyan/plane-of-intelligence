import subprocess as sub

class Manager:
    def __init__(self):
        print("Manager initialized")

    def __del__(self):
        try: self.proc_world.kill()
        except: pass

    def run(self):
        print("Running...")
        self.initWorldProc()

        
        # start world process
        #self.worldproc = sub.Popen(["python", "world.py"], stdin=sub.PIPE, stdout=sub.PIPE, encoding="UTF-8")

        # start AI process

        # send start signal to world
        #self.worldproc.stdin.write("Hi there world!\n")
        #self.worldproc.stdin.flush()
        #
        #stuff = self.worldproc.stdout.readline()
        #while stuff != "!DONE\n":
            #print("Received: " + stuff)
            #stuff = self.worldproc.stdout.readline()
            #
        #self.worldproc.kill()

    def initWorldProc(self):
        print("\nOpening world process...")
        self.proc_world = sub.Popen(["python", "world.py"], stdin=sub.PIPE, stdout=sub.PIPE, encoding="UTF-8")
        print("Process started!")
        
        print("Testing world process I/O...\n")
        self.proc_world_write("ping", True)
        output = self.proc_world_read(True)
        if output != "pong":
            print("\nERROR: I/O Test failed")
            self.errorStop()

        print("\nWorld process I/O test successful!")
            

        
    def proc_world_write(self, msg, log=False):
        if log: print("Manager -> World :: [" + msg + "]")
        self.proc_world.stdin.write(msg + "\n")
        self.proc_world.stdin.flush()
        
    def proc_world_read(self, log=False):
        world_out = self.proc_world.stdout.readline()
        world_out = world_out[:-1] # strip the newline from the end
        if log: print("Manager <- World :: [" + world_out + "]")
        return world_out

    def errorStop(self):
        print("Error stated called for stop")
        exit()
        


# driver bit
m = Manager()
m.run()
print("Manager driver ended")
