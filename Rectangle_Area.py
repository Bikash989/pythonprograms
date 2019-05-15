import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, point):
        return(math.sqrt((math.pow((self.x - point.x),2) + math.pow((self.y - point.y),2))))

class Rectangle:
    def __init__(self,len,breadth):
        self.length = len
        self.breadth = breadth
    def getArea(self):
        return self.length * self.breadth

def main():
    try:
        noOfIterations = int(input())
        while noOfIterations > 0:
            #https://www.geeksforgeeks.org/input-multiple-values-user-one-line-python/
            x1,y1,x2,y2,x3,y3 = map(float, input().split())

            pointA = Point(x1, y1)
            pointB = Point(x2, y2)
            pointC = Point(x3, y3)

            pointsDistance = [pointA.distance(pointB), pointB.distance(pointC), pointC.distance(pointA)]

            pointsDistance.sort()
            rectangle = Rectangle(pointsDistance[0], pointsDistance[1]) #pointsDistance[3] is hypoteneuse, we don't need
            print("Area of rectangle with vertices ({0},{1}),({2},{3}),({4},{5}) is ".format(x1,y1,x2,y2,x3,y3),end='')
            print(round(rectangle.getArea(),4)) #rounding to 4 figure after decimal


            noOfIterations -= 1  #loop variable

    except Exception as ex:
        print('PROGRAM CRASHED, REASON: {0}'.format(ex))


if __name__ == "__main__": main()
