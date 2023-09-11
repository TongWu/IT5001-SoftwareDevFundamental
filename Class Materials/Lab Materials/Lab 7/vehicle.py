class Cannon:
    def __init__(self):
        self.numAmmo = 0
    def fire(self):
        if self.numAmmo:
            print("Fire!!!!!!!")
            self.numAmmo -= 1
        else:
            print("No more ammo")
    def reload(self):
        if self.numAmmo:
            print("Unable to reload")
        else:
            print("Cannon reloaded")
            self.numAmmo += 1

class Vehicle:
    def __init__(self,pos):
        self.pos = pos
        self.velocity = (0,0)

    def setVelocity(self,vx,vy):
        self.velocity = (vx,vy)
    def move(self):
        self.pos = (self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1])
        print(f"Move to {self.pos}")    

class Tank(Vehicle,Cannon):
    def __init__(self,pos):
        Vehicle.__init__(self,pos)
        Cannon.__init__(self)
        
class Sportscar(Vehicle):
    def turnOnTurbo(self):
        print("VROOOOOOOM......")
        self.velocity = (self.velocity[0]*2,self.velocity[1]*2)
        print(f"Velocity increased to {self.velocity}")

class Lorry(Vehicle):
    def __init__(self,pos):
        super().__init__(pos)  
        self.cargo = [] 
    def load(self,cargo):
        self.cargo.append(cargo)
    def unload(self,cargo):
        if cargo in self.cargo:
            self.cargo.remove(cargo)
            print(f"Cargo {cargo} unloaded.")
        else:
            print(f"Cargo {cargo} not found.")
    def inventory(self):
        print("Inventory:"+str(self.cargo))

class Bisarca(Lorry):
    def __convertCargo(self):
        output = []
        for c in self.cargo:
            output.append(str(type(c)).split('.')[1].split('\'')[0])
        return output
    def inventory(self):
        print("Inventory:"+str(self.__convertCargo()))            
    def load(self,cargo):
        if isinstance(cargo,Vehicle):
            super().load(cargo)
        else:
            print(f'Your cargo ({cargo}) is not a vehicle!')

class BattleBisarca(Bisarca,Cannon):
    def __init__(self,pos):
        Bisarca.__init__(self,pos)
        Cannon.__init__(self)

OptimasPrime = BattleBisarca((0,0))
OptimasPrime.load("Food")
                  
myCar = Sportscar((0,0))
myCar.setVelocity(0,40)
myCar.move()
myCar.turnOnTurbo()
myCar.move()


myTruck = Lorry((10,10))
myTruck.setVelocity(10,0)
myTruck.move()
myTruck.load("Food")
myTruck.load("Supplies")
myTruck.inventory()
myTruck.unload("Food")
myTruck.inventory()
myTruck.unload("Gold")

myDadTruck = Bisarca((0,0))
myDadTruck.load("Food")
myDadTruck.load(myCar)
myDadTruck.load(myTruck)
myDadTruck.inventory()
    
