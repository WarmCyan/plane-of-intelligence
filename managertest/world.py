import sys

class World:
    def __init__(self):
        #print("World initialized")
        self.running = True
        pass

    def handleIncoming(self, msg):
        if msg == "ping": self.write_out("pong")
        else:
            self.write_out("wtf?")
            

    def listen(self):
        while self.running:
            incoming = sys.stdin.readline()
            # strip newline
            incoming = incoming[:-1]
            self.handleIncoming(incoming)

    def write_out(self, msg):
        sys.stdout.write(msg + "\n")
        sys.stdout.flush()
            
        



# driver bit

w = World()
w.listen()
#print("World driver ended")

#print("Hi there")
#while running:
    #sys.stdout.write("Hello!\n")
    #sys.stdout.flush()

#while running:
    #sys.stdout.write("Hello!\n")
    #sys.stdout.flush()
    #data = sys.stdin.readline()
    #sys.stdout.write("The world got the following data: " + str(data) + "\n")
    #sys.stdout.flush()
    #sys.stdout.write("!DONE\n")
    
