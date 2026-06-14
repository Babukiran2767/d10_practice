# # Defining a function
# def greet(name):
#     return f"Hello, {name}!"

# # Using the function
# print(greet("Alice"))
# print(greet("Bob"))

# num=int(input('enter your number:'))
# print(num)

# def states(a,b):
#     print(f"{a} is the state of {b}")
# states('hyd','telanagana')
# states(a='AP',b='vizag')

# #arbitary args:  using * sysmble
# def king(*a):
#     print(a)
# king(1,2,3,4,5)
# king('kiran','munny','sidhu')
# king('chicken','biryani') 
# 
# def student_info(name,city,batch='d10'):
#     print(f'{name} is coming from {city} in batch {batch}')
# student_info('kiran','hyd')
# # student_info('munny','orisaa') 
# #  
# # def find_length(x):
# #     count=0
# #     for i in x:
# #      count=count+1
# #     print(count)

# # find_length([4,5,6,7,8])
# # find_length('welcome')
# # find_length('hello world')

# def check_string(s):
#     # Step 1: Check if length is even
#     if len(s) % 2 != 0:
#         return "String length is odd, cannot split evenly."
    
#     # Step 2: Split into two halves
#     mid = len(s) // 2
#     first_half = s[:mid]
#     second_half = s[mid:]
    
#     # Step 3: Count odd digits in each half
#     def count_odds(part):
#         return sum(1 for ch in part if ch.isdigit() and int(ch) % 2 != 0)
    
#     odds_first = count_odds(first_half)
#     odds_second = count_odds(second_half)
    
#     # Step 4: Compare
#     if odds_first == odds_second:
#         return f"Equal odds: {odds_first} in each half."
#     else:
#         return f"Not equal odds: {odds_first} in first half, {odds_second} in second half."

# # Example usage
# print(check_string("123456"))   # Even length, split into "123" and "456"
# print(check_string("2468"))     # Even length, split into "24" and "68"
# print(check_string("13579"))    # Odd length
      

# def func(a,b):
#     return a+b
# print(func(2,3))


