class Car(object):
    def _init_(self, model, colour, company, speed):
        self.colour = colour
        self.model = model
        self.speed = speed
        self.company = company

    def start(self):
        print("dummy")
    
    def stop(self):
        print("stop")
    
    def accelerate(self):
        print("accelerate")

    def changeGear(self, gearType):
        print("gearChange")