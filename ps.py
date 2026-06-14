# # s  = 'Hello World Example'

# # lst = s.split()
# # res =''
# # # print(lst)


# # for word in lst:
# #     temp = ''
# #     for ch in word:
# #         temp = ch + temp
# #     res += temp + ' ' 
# # print(res)       
#     # print(word)


# # example 2/////

# # s  = 'Hello World Example'
# # res = ''
# # temp = ''

# # for ch in s:
# #     if ch != ' ':
# #         temp = ch + temp
# #     else:
# #         res += temp + " "
# #         temp = ''
# # res+=temp
# # print(res) 



# # to find factors
    
# # n = 17
# # c = 0
# # for i in range (1,n+1):
# #     if n%i == 0:
# #         c = c+1
# # print(c)


# # TO FIND PRIME OR NOT

# # n = int(input('Enter your number: '))
# # c = 0
# # for i in range (1,n+1):
# #     if n%i == 0:
# #         c = c+1
# # if c == 2:
# #     print('prime')
# # else:
# #     print('not prime')
# # # print(c)


# # n = 2

# # def is_prime(n):
# #     c = 0
# #     for i in range (1,n+1):
# #         if n%i == 0:
# #             c +=1
# #     if c == 2 :
# #         return True 
# #     else:
# #         return False
# # x = 1
# # while n > 0 :
# #     if is_prime== True:
# #         print(x)
# #         n-=1
# #     x+= 1




# """
# Iterators
# Generators
# decorators
# """

# # Iterators



'''
iterators:
-----
iterator is an object which gives values or elements
one by one from collection.
'''

# # lst = [1,2,3,4,5]  
# # for n in lst :
# #     print(n)

# # lst = [1,2,3,4,5]  # Iterables ( list,tuple,set,dict)
# # itr = iter(lst)    #iterator
# # # print(itr)
# # print(next(itr))
# # print(next(itr))
# # print(next(itr))
# # print(next(itr))
# # print(next(itr))



# # lst = [1,2,3,4,5]
# # itr = iter(lst)

# # while True:
# #     try:
# #         print(next(itr))
# #     except StopIteration:
# #         # print('break point')
# #         break    

# import sys

# # lst = list(range(1,1000))
# # # print(lst)
# # res = [i*2 for i in lst[0:1000]]
# # print(sys.getsizeof(lst))

# itr = iter(range(1,1000))
# res =[next(itr)**2 for i in range (1,11)]
# print(res)
# print(sys.getsizeof(itr))


# lst = list(range(1,100000000))
# res = [i**2 for i in lst[0:10]]
# print(lst)


# itr = iter (range(1,100000000))
# # print(next(itr))
# res =[next(itr) **2 for i in range (1,10000000)]
# print(res )


# s = 'Nayab'
# # s= {1:'one',2:'two',3:'three'}
# s= {1:'one',2:'two',3:'three'}.items()
# itr = iter(s)
# print(next(itr))
# # print(next(itr))
# # print(next(itr))
# # # print(next(itr))
# # # print(next(itr))

# class MyIterator:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self  

#     def __next__(self):
#         if self.start <= self.end:
#             val =  self.start
#             self.start += 1
#             return val
#         else:
#             raise StopIteration
        
# obj = MyIterator(1,5)
# itr = iter(obj)   # iterable
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# # print(next(itr))


# class EvenIterator:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self  

#     def __next__(self):
#         if self.start <= self.end:
#             val =  self.start
#             self.start += 2
#             return val
#         else:
#             raise StopIteration
        
# Even = EvenIterator(2,100)
# itr = iter(Even)   # iterable
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


'''
Generator
---------
Generator is a special iterator object which gives elements
one by one from a collection using  'yield' keyword.

Properities of Iterator and Generator:
-------------------------
1) Gives values one by one
2) Less Memory Usage
3) Lazy Evaluation
'''
# class Number:
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return self


#     def __next__(self):
#         if self.start <= self.end: 
#             val = self.start
#             self.start += 1
#             return val
#         else :
#             raise StopIteration
        
# n = Number(1,10) 
# # print(next(iter(n)))    
# for i in n :
#     print(i)


# def genc():
#     yield 1
#     yield 2
#     yield 3
#     return StopIteration

# g = genc()    
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))



# def gen(start,end):
#     while start <= end:
#         yield start 
#         start += 1
        
# g = gen(1,5)   
# print(next(g))     
# print(next(g))
# print(next(g))



# def gen():
#    yield 1
#    yield 3
# g = gen()   
# print(next(g))     
# print(next(g))
# print(next(g))


# class Number :
#     def __init__(self,start,end):
#         self.start = start
#         self.end = end


#     def gen(self):
#         while self.start <= self.end:
#             yield self.start
#             self.start += 1

# n = Number (1,11)
# g = n.gen()
# print(next(g))            
# print(next(g))  
# print(next(g))  
# print(next(g))  


''''
Decorator
------------------
Decorator is a function which used to change the 
behaviour of another function without changing its
code.


'''

# def outer(func):
#     def wrapper():
#         print('Before func call')
#         func()
#         print('After func call')
#     return wrapper

# # @outer
# def greet():
#     print('hello')
# greet = outer(greet)
# greet()    

# def check_credentials(func):
#     def inner():
#         username = input("Enter your username: ")
#         password = input("Enter your password: ")
#         if username == 'user@123' and password == 'password@123' :
#             func()
#         else:
#             print('Access Denied')
#     return inner
# @check_credentials            
# def dashboard():
#     print('welcome to dashboard....')


# dashboard() 
# dashboard = check_credentials(dashboard)
# dashboard()   