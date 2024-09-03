'''How does encapsulation in the Pen and Ink classes improve the management of the ink 
   reservoir, and what are the benefits of this approach in terms of data integrity, code maintenance, and usability?'''

#---------------------------------Ink Class---------------------------------#
class Ink:
    def __init__(self, volume):
        self.volume = volume

    def refill(self, amount):
        if amount > 0:
            self.volume += amount
            print(f"Total Refill Volume")
        else:
            print("Refill already present")

    def use(self, amount):
        if amount > 0 and self.volume >= amount:
            self.volume -= amount
            print(f"Ink Used :{amount} & left refill volume : {self.volume}.")
            return True
        elif amount <=0:
            print("Used ink")
            return False
        else:
            print("No Ink Please refill it !")    
            return False

    def get_volume(self):
        return self.volume
    
#----------------------------------Pan Class-----------------------------------#
class Pen:
    def __init__(self, ink_vloume):
        self.ink = Ink(ink_vloume)

    def write(self, amount):
        if self.ink.use(amount):
            print(f" Wrote ink {amount}")
    
    def  refill_ink(self, amount):
        self.ink.refill(amount)

    def check_ink_level(self):
        print(f"The level of Ink is : {self.ink.get_volume()}")  

pen = Pen(20)
pen.write(8)
pen.refill_ink(6)
pen.check_ink_level()
