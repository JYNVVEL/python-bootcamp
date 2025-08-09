class Door:
    def __init__(self, closed=False):
        self.closed = closed

    def open(self):

        if self.closed == False:
            print("Door is already open")
        self.closed = False


    def close(self):
        if self.closed == True:
            print("Door is already closed")
        self.closed = True


door = Door()
door.open()
door.close()