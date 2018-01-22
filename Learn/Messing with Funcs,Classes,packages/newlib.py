class wizard(object):

    _spell = "Stupefy"

    def __init__(self) :
        print("Hello")
    
    def cast(self,a=""):
        if not a=="":
            self.spell = a
        
        print(self.spell)

    def attack(self):
        temp = wizard._spell
        print(temp)


obj = wizard()
obj.attack()
