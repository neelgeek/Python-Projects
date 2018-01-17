class wizard(object):

    spell = "Stupefy"

    def __init__(self) :
        print("Hello")
    
    def cast(self,a=""):
        if not a=="":
            self.spell = a
        
        print(self.spell)


