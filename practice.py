
# '''
# what is python?
# python is intrepreted higlevel prorgraming language 
# easy to learn
# 2.python IDEs (intregrated development environment)
# it used to edit and run python code easily
# 3.python simple code 
# '''
# # #3. 
# # print("hello world")

# # # 2.SYNTAX AND SEMANTICS

# #1.Syntax
# # print("hello kiran!")  #correct syntax
# # print "hello wokrd"    #wrong syntax

# #2.semantics(semantics is syntax is correct and logic must also be correct)

# # a=10
# # b=15
# # print(a+b)

# #3.VARIABLES AND DATA TYPES

# #(variable is a container to store the data)

# # x=30
# # name="kiran"

# # print(x,name) #x and name store the some value that is called variable



# ''' 
# 1.int ---->all types of number whole numbers positive/negative
# 2.float---->it contains decimal values
# 3.string----it text data must be in double and single quotes
# 4.boolean--->true or false
# '''
# #int
# # a=30
# # b=20
# # print(a+b)

# #float
# # de=3.33
# # f=4.3
# # print(de,f)

# #string
# # name="kiran"
# # wish="happy birthday"
# # print(name,wish)

# #boolean

# # value1=True
# # value2=44
# # print(isinstance(value1,bool))
# # print(isinstance(value2,bool))

# #BASIC INPUT AND OUTPUT
# # print("hello word")

# # #input method  (take input from users)
# # num=int(input("enter your number:"))
# # print(num)

# # 3.ARHTEMATIC OPERATIONS(+,-,*,%,)


# #============= class 08-06-2026====================

# # lst = [1, 2, 3, 4]
# # result = []

# # for i in range(len(lst)):
# #     product = 1
# #     for j in range(len(lst)):
# #         if i != j:
# #             product *= lst[j]
# #     result.append(product)

# # print(result)  


# lst = [1,2,3,4]
# res =[]
# prod=1
# for i in lst:
#     prod= i*prod
# for i in lst:
#     res.append(prod)
# print(res)        

# lst = [15,7,2,9,6]
# t = 1
# res = []
# for i in range (len(lst)-1):
#     for j in range(i+1,len(lst)):
#         cur_sum = lst[i]+lst[j]
#         if cur_sum == t:
#             res.append((i,j))
# print(res)            





