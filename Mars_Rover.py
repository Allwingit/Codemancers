

class Mars:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.poisition_occupied =[]

class Rover:
    def __init__(self,x,y,direction):
        self.x=x
        self.y=y
        self.direction=direction

    def current_position(self):
        return self.x,self.y,self.direction

    def left(self):

        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"

        print (self.x, self.y,self.direction)

    def right(self):

        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

        print (self.x, self.y,self.direction)

    def forward(self,mars):

        if self.direction == "N":
            if int(self.y) < int(mars.y):
                self.y = int(self.y) + 1

        elif self.direction == "S":
            if int(self.y) > 0:
                self.y = int(self.y) - 1

        elif self.direction == "E":
            if int (self.x) < int(mars.x):
                self.x = int(self.x) + 1

        elif self.direction == "W":
            if int(self.x) > 0:
                self.x = int(self.x) - 1

        print (self.x, self.y,self.direction)

def rover_move(plannet,rover):

    command = input("Rover Movement command : ")
    for cmd in command:
        if cmd == 'L':
            rover.left()
        elif cmd == 'R':
            rover.right()
        elif cmd == 'M':
            rover.forward(plannet)




def main():
    loop=1
    bountries= input("Mars platue size : ").split()
    mars=Mars(bountries[0],bountries[1])

    while loop ==1:
        init_position = input("Rover Initial Position :").split()
        rover= Rover(init_position[0],init_position[1],init_position[2])
        rover_move(mars,rover)
        mars.poisition_occupied.append(init_position)
        print (rover.current_position())


if __name__== "__main__":
    main()
