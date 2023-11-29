class RGB():
    def __init__(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        self.grade = None
        self.chargrade = None

    def dictgrade(self):
        return {
            'R': self.r,
            'G': self.g,
            'B': self.b,
            'Grade': self.grade,
            'Maturity': self.chargrade
        }
    
    def evaluate(self):
        if ((self.r > self.g) and ((self.r - self.g) < 9)) and (self.g >= 142):
            self.grade = 3
            self.chargrade = 'Good'
        elif ((self.r > self.g) and ((self.r-self.g) >= 9)) and (self.g >= 142):
            self.grade = 5
            self.chargrade = 'Great'
        elif (self.r > self.g) and (self.g <= 142):
            self.grade = 7 
            self.chargrade = 'Throw away'
        elif (self.g > self.b):
            self.grade = 1
            self.chargrade = 'Not yet eatable'
        return self.grade



if __name__ == '__main__':
    banana = RGB(105,240,187)
    banana.evaluate()
    print(banana.grade)
    print(banana.dictgrade())

