# --------> TIME COMPLEXITY <-----

# num = int(input("enter your number:"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")   


arr =[1,2,3,4,5]
i = 0
j =arr.length-1
while (i<j):
    temp = arr(i)
    arr(i)=arr(j)
    arr(j)=temp
print(arr)    