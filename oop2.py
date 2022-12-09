class Rectangle:
 def __init__(self, length, width):
   self.length = length
   self.width = width

 @property
 def length(self):
   return self.__length

 @property
 def width(self):
   return self.__width

 @length.setter
 def length(self, length):
  if length <= 0:
    self.__length = -length + 1
  else:
    self.__length = length

 @width.setter
 def width(self, width):
  if width <= 0:
   self.__width = -width + 1
  else:
   self.__width = width

# Todo: calculating area of rectangle
 def cal_area(self):
  return self.__length * self.__width

# Todo: calculating perimeter of rectangle
 def cal_perimeter(self):
  return 2 * (self.__length + self.__width)


 if __name__ == '__main__':
  rec_1 = Rectangle(-10,-5)
  print("Rectangle 1")
  print(rec_1.length, "*", rec_1.width)

rec_2 = Rectangle(10, 5)
area = rec_2.cal_area()
perimeter = rec_2.cal_perimeter()
print("Rectangle 1")
print(rec_2.length, "*", rec_2.width)
print("Area:", area)
print("perimeter:", perimeter)
