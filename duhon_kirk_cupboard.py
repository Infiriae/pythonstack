class Cup:
    counter = 0
    def __init__(self,materialofcup,colorofcup):
        Cup.counter+=1
        self.material = materialofcup
        self.color = colorofcup
        self.percent_filled = 0

    def fill(self,amount):
        self.percent_filled+=amount
        return self

    def pour(self,amount):
        self.percent_filled-=amount
        return self

    def spill(self):
        self.percent_filled = (self.percent_filled/2)
        return self

    def info(self):
        print(f'the #{self.counter} cup is {self.color} and made of {self.material} and is {self.percent_filled}% full')
        return self

mycup = Cup("glass","green")
hercup = Cup("porcelain","purple")


mycup.fill(20).fill(20).fill(20).spill().fill(20).pour(12).info()
#mycup.info()