class Student:
    def __init__(self): #default constructor
        self.id=0
        self.name='unknow'
        self.place= 'earth'

# s= Student() 
# s.id =1
# s.name='kiran'
# s.place='mandpeta'     
# print(Student)


# class Number:
#     def __init__(self,a,b,c,d):
#         self.a=a
#         self.b=b
#         self.c=c
#         self.d=d
#         print(self.a+self.b+self.c+self.d)

# n1=Number(10,20,30,40)     


# class Number:
#     def __init__(self,*nums):
#         if len(nums) == 0:
#             print('default contructor')
#         elif len(nums) == 1:
#            self.a = nums[0]
#            print(self.a)   
#         elif len(nums) == 2:
#             self.a=nums[0]
#             self.b =nums[1]
#             print(self.a+self.b)
#         elif len(nums) == 3:
#             self.a=nums[0]
#             self.b=nums[1]
#             self.c=nums[2]
#             print(self.a+self.b+self.c)
#         else :
#             print(sum(nums))  

# n1=Number(10) 
# n2=Number(10,20)
# n3=Number(10,20,30)      
# n1=Number(10,20,30,40)  


# class Teacher:
#     def teach (self):
#         print('teacher can teach')
#     def take_attendence(self):
#         print('take attanedence')


# class Physics_Teacher(Teacher):
#     def teach (self):
#         print('teacher can teach')
#     def take_attendence(self):
#         print('take attanedence')  


# class BiologyTeacher():
#     def teach (self):
#         print('teacher can teach')

#     def take_attendence(self):
#         print('take attanedence')  

# a=Teacher()
# a.teach()
# a.take_attendence()
# print('='*22)
# e=Physics_Teacher()
# e.teach()
# e.take_attendence()
# print('='*22)
# B=BiologyTeacher()
# B.teach()
# B.take_attendence()


# 27 class 

# class attribute
# class Student:
#     clg_name='10k college'  #class attribute
#     def __init__(self,id,name,a):
#         self.id =id   #instance attribute
#         self.name =name
#         age = a # 3.local Attribute
#         print(age)

# s=Student(1,'kiran',24)   
# print(s.id)
# # print(s.name)
# # # print(s.age) 
# # print(s.clg_name)  
# # print('='*22)  

# # s=Student(2,'munny',23)   
# # print(s.id)
# # print(s.name)
# # # print(s.age) 
# # print(s.clg_name)    

# # print('='*22)
# # s=Student(3,'sidhu',22)   
# # print(s.id)
# # print(s.name)
# # # print(s.age) 
# # print(Student.clg_name)    


# # 2.instance Attribute
# # 3.local Attribute


# # CLASS METHOD 

# # ////////


# from abc import ABC, abstractmethod
# class PayementProcess(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
# class UPI(PayementProcess):
#     def pay (self,amount): 
#         print('amount',amount,'paid using upi...!') 
# class debitcard(PayementProcess):
#     def pay(self,amount):
#         print('amount',amount,'paid using debitcard')          
# class netbanking(PayementProcess):
#     def pay(self,amount):
#         print('amount',amount,'paid using netbanking')

# upi=UPI()
# upi.pay(1000)


# dc= debitcard()
# dc.pay(1000)

# nb=netbanking()
# nb.pay(103930)


# class calculator(ABC):
#    @abstractmethod
#    def addtion(self,a,b):
#      pass
   
#    @abstractmethod
#    def subtraction(self,a,b):
#      pass
   
#    @abstractmethod
#    def multiplication(self,a,b):
#      pass



# class clientcalculator(calculator):
#     def additon(self,a,b):
#       print(a+b)

#     def subtraction(self,a,b):
#       print(a-b)

#     def multiplication(self,a,b):
#       print(a*b)

# cc=clientcalculator()
# cc.additon(2,3)
# cc.subtraction(50,100)      
# cc.subtraction(40,40)


 