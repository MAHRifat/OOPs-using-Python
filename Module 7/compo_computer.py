class CPU:
    def __init__(self,cores):
        self.cores = cores

class RAM:
    def __init__(self,rsize):
        self.rsize=rsize

class Hard_Drive:
    def __init__(self,capacity):
        self.capacity=capacity

class Laptop:
    def __init__(self,cores,rsize,capacity):
        self.cpu=CPU(cores)
        self.ram=RAM(rsize)
        self.hardDrive=Hard_Drive(capacity)

