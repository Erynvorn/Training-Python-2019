class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
    def guess(self,n):
        self.n = n
        if self.n == self.number :
            return True
        else :
            self.lives -+ 1
            if self.lives < 1 : raise Exception("Omae wa mo shindeiru") 
            #pass #throw exception
        return False
