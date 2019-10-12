class ModList:
    def __init__(self, l):
        self.list = l
    def append(self,val):
        self.list.append(val)
    
    def __add__(self,other):
        if(type(self).__name__ == type(other).__name__):                
            res = [] #empty list
            for a,b in zip(self.list,other.list):
                res.append(a+b)
            return res    
        else:
            return ModList([val + other for val in self.list])

     # overloading - op
    def __sub__(self,other):
        if(type(self).__name__ == type(other).__name__):                
            res = [] #empty list
            for a,b in zip(self.list,other.list):
                res.append(a - b)
            return res    
        else:
            return ModList([val - other for val in self.list])
             # overloading - op
    def __mul__(self,other):
        if(type(self).__name__ == type(other).__name__):                
            res = [] #empty list
            for a,b in zip(self.list,other.list):
                res.append(a * b)
            return res    
        else:
            return ModList([val * other for val in self.list])
             # overloading - op
    def __truediv__(self,other):
        if(type(self).__name__ == type(other).__name__):                
            res = [] #empty list
            for a,b in zip(self.list,other.list):
                res.append(a / b)
            return res    
        else:
            return ModList([val / other for val in self.list])
             # overloading - op
    def __floordiv__(self,other):
        if(type(self).__name__ == type(other).__name__):                
            res = [] #empty list
            for a,b in zip(self.list,other.list):
                res.append(a // b)
            return res    
        else:
            return ModList([val // other for val in self.list])
    def __pow__(self,other):
            if(type(self).__name__ == type(other).__name__):                
                pass #return error   
            else:
                return ModList([val ** other for val in self.list])

    def __repr__(self):
        return '{}'.format(self.list)


a = ModList([10,25,60])
b = ModList([2,6])
print(a)
print(a/b)
print(a//b)
print(a*b)
print(a ** 2)

# bonus part, unable to implement
x = list()
y = list()
x.extend([1,2,3])
y.extend([1,2,3])
print(x+y)