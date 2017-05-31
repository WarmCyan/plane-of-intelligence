import subprocess as sub
import time

class Manager:
    def __init__(self):
        print("Manager initialized")

    def __del__(self):
        try: self.proc_world.kill()
        except: pass

    def run(self):
        print("Running...")
        self.initWorldProc()
        self.latencyReport()


    def initWorldProc(self):
        print("\nOpening world process...")
        self.proc_world = sub.Popen(["python", "world.py"], stdin=sub.PIPE, stdout=sub.PIPE, encoding="UTF-8")
        print("Process started!")
        
        # make sure io is working
        print("Testing world process I/O...\n")

        self.proc_world_write("!ping", True)
        #starttime = time.clock()
        output = self.proc_world_read(True)
        #iotime = (time.clock() - starttime)*1000
        if output != "!pong":
            print("\nERROR: I/O Test failed")
            self.errorStop()
        #print("(Response time: %.3f ms)" % iotime)

        print("\nWorld process I/O successful!")
            
    def latencyReport(self, testsize=100, largetestsize=2):
        print("\nRunning latency tests...")

        print("Preparing large messages...")
        self.proc_world_write("!createtests")
        
        largemsg = "*"
        largemsg *= 50000
        largemsg = ":" + str(largemsg)
        
        excessivemsg = "*"
        excessivemsg *= 5000000
        excessivemsg = ":" + str(excessivemsg)

        print(self.proc_world_read())
        print("Large tests ready!")
        
        print("\nLatency Report:\n--------------------")

        # single ping
        singlerw_avg = 0
        for i in range(0, testsize):
            singlerw_start = time.clock()
            self.proc_world_write("!ping")
            self.proc_world_read()
            singlerw = (time.clock() - singlerw_start)*1000
            singlerw_avg += singlerw
        singlerw_avg /= testsize
        
        print("Single ping response: %.3f ms" % singlerw_avg)

        # 1000 pings
        multirw_avg = 0
        for i in range(0, largetestsize):
            multirw_start = time.clock()
            i = 0
            while i < 1000:
                self.proc_world_write("!ping")
                i += 1
            j = 0
            while j < 1000:
                self.proc_world_read()
                j += 1
            multirw = (time.clock() - multirw_start)*1000
            multirw_avg += multirw
        multirw_avg /= largetestsize
        
        print("1000 pings response: %.3f ms" % multirw_avg)

        # large message
        largew_avg = 0
        for i in range(0, testsize):
            largew_start = time.clock()
            self.proc_world_write(largemsg)
            self.proc_world_read()
            largew = (time.clock() - largew_start)*1000
            largew_avg += largew
        largew_avg /= testsize
        
        print("\nLarge write (~50KB): %.3f ms" % largew_avg)
        
        # large read
        larger_avg = 0
        for i in range(0, testsize):
            larger_start = time.clock()
            self.proc_world_write("!largetest")
            self.proc_world_read()
            larger = (time.clock() - larger_start)*1000
            larger_avg += larger
        larger_avg /= testsize
        
        print("Large read (~50KB): %.3f ms" % larger_avg)
        
        # excessive message
        excessivew_avg = 0
        for i in range(0, largetestsize): # hard limited at 10, to avoid taking forever!
            excessivew_start = time.clock()
            self.proc_world_write(excessivemsg)
            self.proc_world_read()
            excessivew = (time.clock() - excessivew_start)*1000
            excessivew_avg += excessivew
        excessivew_avg /= largetestsize
        
        print("\nExcessive write (~5MB): %.3f ms" % excessivew_avg)
        
        # excessive read
        excessiver_avg = 0
        for i in range(0, largetestsize):
            excessiver_start = time.clock()
            self.proc_world_write("!excessivetest")
            self.proc_world_read()
            excessiver = (time.clock() - excessiver_start)*1000
            excessiver_avg += excessiver
        excessiver_avg /= largetestsize
        
        print("Excessive read (~5MB): %.3f ms" % excessiver_avg)

        print("--------------------")
        
        self.proc_world_write("!deletetests")
        print(self.proc_world_read())


        print("")

        
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
        print("Error state called for stop")
        exit()
        


# driver bit
m = Manager()
m.run()
print("Manager driver ended")
