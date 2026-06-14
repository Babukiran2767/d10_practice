# num=153
# while num//10>0:
#     print(num)


#TABLE

# num=int(input('enter your number:'))
# i=1
# while i<=10:
#     print(num,'*',i,'=',num*i)    #5*1=5
#     i=i+1

#LEAP YEAR BETWEEN 3679 TO 5690

# year=3679
# while year<=5690:
#     if (year%4==0 and year%100!=0) or (year%400==0):
#         print(year)
#     year=year+1

# MULTIPLE OF 3
# IF YES CHECK MULTIPLE OF 7 AND 9
# IF NOT CHECK MULTIPLE OF 4 AND 12

# num=int(input('enter your number:'))
# if num%3==0:
#     if num%9==0 and num%7==0:
#      print('divsible of 7 and 9')
#     else:
#        pass 
# else :
#     if num%4==0 and num%12==0:
#       print('divsible of 4 and 12')

# strength=int(input('enter your strength of students:'))
# no_sections=int(input("enter number of sections:"))

# each_section=strength//no_sections
# extra=strength%no_sections
# i=1
# while i<=no_sections:
#     if i==no_sections:
#         print('section',i,'-',each_section+extra)
#     else:
#         print('section',i,'-',each_section)    
# i=i+1        


# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.symmetric_difference(s2))






# class parent:
#     def eat(self):
#         print("he is eating")
#     def sleep(self):
#         print("he was sleeping")

# class child(parent):        
#     def walk(self):
#         print("walking")   
#     def main(self):
#         print("this is main")  


# class munny_child(child) :
#     def habits(self):
#      print("this is all good habits")  



# s= munny_child()
# s.eat()
# s.sleep()
# s.walk()
# s.main()
# s.habits()



