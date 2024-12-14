#Create a calculator to calculate areas


def add():
 a=int(input("Enter your first number: "))
 b=int(input("Enter your second number: "))
 c=a+b
 print(a," + ",b,"is equals to: ",c)
 return c
def sub():
 a=int(input("Enter your first number: "))
 b=int(input("Enter your second number: "))
 c=a-b
 print(a," - ",b,"is equals to: ",c)
 return c
def mul():
 a=int(input("Enter your first number: "))
 b=int(input("Enter your second number: "))
 c=a*b
 print(a," x ",b,"is equals to: ",c)
 return c
def div():
 a=int(input("Enter your first number: "))
 b=int(input("Enter your second number: "))
 c=a/b
 print(a," / ",b,"is equals to: ",c)
 return c
def tri():
 b=int(input("Enter the base: "))
 h=int(input("Enter the height: "))
 c=((1/2)*b)*h
 print("The area of the triangle is: ",c)
 return c
def squ():
 b=int(input("Enter the base: "))
 c=b*b
 print("The area of the square is: ",c)
 return c
def rect():
 b=int(input("Enter the base: "))
 h=int(input("Enter the height: "))
 c=b*h
 print("The area of the rectangle is: ",c)
 return c
def circ():
 a=int(input("Enter the radius of the circle: "))
 
 c=(24/7)*a*a
 print("The area of the circle is: ",c)
 return c
def trap():
 a=int(input("Enter the length of the first side: "))
 b=int(input("Enter the length of the second side: "))
 h=int(input("Enter the height of the trapezuim"))
 c=(1/2)*(a+b)*h
 print("The area of the trapezium is: ",c)
 return c
def para():
 b=int(input("Enter the base: "))
 h=int(input("Enter the vertical height: "))
 c=b*h
 print("The area of the parallelogram is: ",c)
 return c


print("************************************************************")
print("***************CALCULATOR***************")
cnt=0
while cnt<20:
 print("Please choose which operation you would like to carry out:")
 print("(1)Regular calculations (2)Area of shapes (3)Exit the program")
 t1=int(input("Enter your choice: "))

 if t1 ==1:
  print("(1)Addition (2)Subtraction (3)Multiplication (4)Division")
  t1=int(input("Enter your choice: "))
  if t1== 1:
   add()
   continue
  elif t1==2:
   sub()
   continue
  elif t1==3:
   mul()
   continue
  elif t1==4:
   div()
   continue
  else:
   print("YOu have entered the wrong number.")
   continue
 elif t1==2:
  print("Enter shape whose area you wish to find: ")
  t1=print("(1)Triangle (2)Square (3)Rectangle (4)Circle (5)Trapezium (6)Parralellogram")
  t1=int(input("Enter your choice: "))
  if t1==1:
   tri()
   continue
  elif t1==2:
   squ()
   continue
  elif t1==3:
   rect()
   continue
  elif t1==4:
   circ()
   continue
  elif t1==5:
   trap()
   continue
  elif t1==6:
   para()
   continue
  else: 
   print("You have entered the wrong number")
   continue
 elif t1==3:
  print("You have exited the program")
  break
 else:
  print("You have entered the wrong operation")
 cnt+=1
 