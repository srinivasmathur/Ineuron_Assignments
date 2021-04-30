class Triangle:
  def __init__(self):
    self.sides=[0]*3
    # print('Base class contructor')

  def inputSides(self):
    for i in range(3):
      self.sides[i] = int(input(f"Enter side {i+1} : "))

class Area(Triangle):
  
  # def __init__(self):
  #   Triangle.__init__(self)
  #   print('inherited')

  def get_area(self):
    a,b,c = self.sides
    s = (a+b+c)/2
    return round((s*(s-a)*(s-b)*(s-c))**0.5,4)

if __name__ == '__main__':
  a = Area()
  a.inputSides()
  print("Area of the triangle : ",a.get_area())