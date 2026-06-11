# class Robo:
#     def walk(self):
#         print("walking")

#     def talk(self):
#         print("talking")

#     def charge(self):
#         print("charging") 


# class fighterobo(Robo):
#   pass

# class teacherobo(Robo):
#    pass

# class driverrobo(Robo):
#     pass

# f=fighterobo() 
# f.walk()
# f.talk()
# f.charge()
# print('='*22)

# t=teacherobo()
# t.charge()
# t.talk()
# t.walk()

# print('='*22)

# d=driverrobo()
# t.charge()
# t.talk()
# t.walk()



# #duck typing


# def access_robot(r):
#     r.talk()
#     r.walk() 
#     r.charge()

# f=fighterobo()
# access_robot(f)
# print('='*22)

# t=teacherobo()
# access_robot(t)
# print('='*22)

# d=driverrobo()
# access_robot(d)


##METHOD OVERRIDING

# class Animal:
#     def sound(self):
#       print("animal make sound")

# class cat(Animal):
#         def sound1(self):
#          print('cat make meow')    
# class dog(Animal):
#         def sound2(self):
#          print("dog make bark")


# c=cat()
# c.sound()
# c.sound1()

# print('='*22)

# d=dog()
# d.sound()
# d.sound2()


#METHOD OVERLOADING

# class calculator:
#     def add(self,a):
#         print(a)
#     def add(self,a,b):
#         print(a+b)
#     def add (self,a,b,c):
#         print(a+b+c) 
#     def add(self,a,b,c,d):
#         print(a+b+c+d)


# c=calculator()
# c.add(10)
# c.add(10,20)
# c.add(10,20,30)
# c.add(10,20,30,40)


# class calculator:
#     def add(self,a=0,b=0,c=0,d=0):
#         print(a+b+c+d)

# c=calculator()
# c.add(10)
# c.add(10,20)
# c.add(10,20,30)
# c.add(10,20,30,40)

# class calculator:
#     def add(self,*num):
#         print(sum(num))

# c=calculator()
# c.add(10)
# c.add(10,20)
# c.add(10,20,30)
# c.add(10,20,30,40)
# c.add(10,20,30,40,50,60,70,80,80,90,100)

#METHOD OVERRIDING

# class Animal:
#     def sound(self):
#         print('animal make sound')

# class Dog (Animal):
#     def sound(self):
#         print('bark') 

# class Cat(Animal):
#     def sound(self):
#         print('meow')

# d=Dog()
# d.sound()

# c=Cat()
# c.sound() 



# class Calculator:

#     def add(self,a):
#          print(a)

#     def add(self,a,b):
#         print(a+b)


#     def add(self,a,b,c):
#         print(a+b+c)

#     def add (self,a,b,c,d):
#         print(a+b+c+d)


# c=Calculator()
# c.add(10)
# c.add(10,20)
# c.add(10,20,30)
# c.add(10,20,30,40)



# class Calculator:

#     def add(self,a):
#          print(a)

#     def add2(self,a,b):
#         print(a+b)


#     def add3(self,a,b,c):
#         print(a+b+c)

#     def add4(self,a,b,c,d):
#         print(a+b+c+d)


# c=Calculator()
# c.add(10)
# c.add2(10,20)
# c.add3(10,20,30)
# c.add4(10,20,30,40)


# class Calculator:

#     def add(self,a=0,b=0,c=0,d=0):
#         print(a+b+c+d)

# # c=Calculator()
# # c.add(10)
# # c.add(10,20)
# # c.add(10,20,30)
# # c.add(10,20,30,40)


# # encapsulation  security
# class Bank:
#     def __init__(self,ac_name,pin):
#         self.ac_name = ac_name
#         self.__pin=pin
#         self.password=1234


#     #  getter
#     def get_pin(self):
#         password= int(input('enter your password:'))
#         if password == self.__password:
#          return self.__pin
#         else:
#             return 'Access denied'
#     #  setter 
#     def set_pin(self,new_pin):
#       password= int(input('enter your password:'))
#       if password == self.__password:
#           self.__pin=new_pin
#       else:
#          print('Access denied')   


 
# b =Bank('ramesh',1947)
# # print(b.pin)
# # print(b.__pin)

# print(b.get_pin())
# # b.set_pin(2222)
# # print(b.get_pin())


class Parent:
    def __int__(self):
        self.data = 'parent data'

    def details(self):
        print(self.data)    

p = Parent()     
p.details()  