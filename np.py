import numpy as np
# import time

# L=list(range(10000000))
# start = time.time()
# res=[x*2 for x in L]
# last_time = time.time()-start

# L1 = np.arange(1000000)
# start = time.time()
# res = L1 * 2
# np_time= time.time()-start  

# print(last_time)
# print(np_time)

# Built-in Methods

# zero = np.zeros((3,3))  # astype(int) >>>> to convert decimal value into integer
# one = np.ones((2,4))
# ar = np.arange(0,10,2)
# ar = np.arange(1,10)

# print(zero)
# print(one)
# print(ar)
# print(ar)

# lin=  np.linspace(0,2,5)
# print(lin)

# iden = np.eye(3) #daigonals became 1
# print(iden)  


# Random


# randf = np. random.rand(2,3)
# print(randf)

# randint= np.random.randint(1,100, size=(4,4))
# print(randint)

# randn=np.random.randn(5)
# print(randn)

# arr= np.array([1,2,3,4,5,6,7,8,9])
# print(np.random.choice(arr,5))


# ar = np.array(
#     [ 
#     [0,0,0],
#     [1,1,1]
#     ],
#     [
#     [2,2,2],
#     [3,3,3]
#     ] 
#     )
# print(ar)


# 3 dimension ----> (BLOCK,ROW, COLUMN)

# arr = np.array([
#     [
#     [1,2,3],
#     [4,5,6]
#     ],
#     [
#        [7,8,9],
#        [1,2,3]  
#     ],
#     [
#         [1,2,3],
#         [3,4,5]
#     ]
# ]
# )

# print(arr.ndim)
# print(arr.shape)


# arr = np.array( [[1,2,3]],order='C')
# print(arr)
# print(arr.flags)



# arr = np.array([21,22,22,23,24,25])
# print(arr)
# print(np.median(arr))
# print(np.var(arr))
# print(np.std(arr))

# print(np.sum(arr))


# =============

# Array Attributes and indexing

# 
# # arr = np.array([10,20,30])
# arr = np.array([[10,20,30],
#                 [40,50,60],
#                 [70,80,90]])
# print(arr)
# arr_shape=arr.shape
# arr_size= arr.size
# arr_ndim =arr.ndim


# print(arr_shape)
# print(arr_size)
# print(arr_ndim)

# Indexing and slicing example

# arr=np.array([[10,20,30],    #[00,01,02]  [rows,column]
#               [40,50,60],    #[10,11,12]
#               [70,80,90]])   #[20,21,22]
# # item = arr[0,1]
# sub = arr[1:,1:]
# # col2 =arr[:,1]
# # col3=arr[:,2]
# col4 = arr[1:,:]


# # print(arr)
# # print(item)
# print(sub)
# # print(col2)
# print(col4)


# ==============
# Mathematical Operation (Vectorized)

# a=np.array([1,2,3])
# b=np.array([4,5,6])

# # add=a+b
# print(add)

# sub=a-b
# print(sub)

# mul=a*b
# print(mul)

# sq=a**2
# print(sq)

# sqr_a=np.sqrt(a)
# sqr_b=np.sqrt(b)

# print(sqr_a)
# print(sqr_b)

# sum_a =np.sum(a)
# print(sum_a)


# =======================
# Usefull Array Methods:
# (min,max,mean,median,std,axis,operations)

# arr = np. array([[10,20,30],[40,50,60]])


# minm=np.min(arr)
# maxm=np.max(arr)
# mean =np.mean(arr)
# median =np.median(arr)
# std_arr= np.std(arr)  #standard deviation
# col_sum=np.sum(arr,axis=0)
# row_sum=np.sum(arr,axis=1)

# print(maxm)
# print(minm)
# print(mean)
# print(median)
# print(std_arr)
# print(col_sum)
# print(row_sum)

# =========================
# BroadCasting & Reshaping

# arr=np.array([[1,2,3],[4,5,6]])

# add_scalar = arr +10

# a = np.arange(12)
# resp=a.reshape(3,4)

# flt=resp.flatten()


# print(a)
# print(resp)
# print(flt)
# print(add_scalar)



# a =np.array([1,2,3])
# b =np.array([4,5,6])
# arr =np.array([10,20,30,40,50,60])
# sor=np.array([10,202,303,430,50,60])

# concat = np.concatenate((a,b))
# vstack=np.vstack((a,b))
# hstack =np.hstack((a,b))
# splits = np.split(arr,4)
# sorted_arr=np.sort(sor)


# print(concat)
# print(vstack)
# print(hstack)
# print(splits)
# print(sorted_arr)

# arr = np.arange(10,1,-1)
# print(arr)

# ones =np.ones((2,2),dtype=int)
# print(ones)

# arr = np.zeros((5,3),dtype=int)
# print(arr)

# arr = np.full((5,7),5)
# print(arr)


# arr = np.eye(5,5,dtype=int)
# print(arr)

# arr = np.linspace(10,100,10)
# print(arr)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# arr1=arr.reshape(6,2)
# print(arr1)
# arr2= arr.flatten()
# print(arr2)



# arr =np.array([1,2,3,4,5])
# print(arr[::-1])


# arr = np.array([10,20,30,40,50])
# print(np.mean(arr))
# print(np.median(arr))

# print(np.var(arr))
# print(np.std(arr))


# arr =np.array([1,2,3,4,5,6,7,8,9,10])
# np.random.shuffle(arr)
# print(arr)


# arr =np.array([
#            [1,2,3],
#            [4,5,6],
#            [7,8,9]

# ])
# k=np.max(arr,axis=1) #vertical
# m=np.max(arr,axis=0)  #horizontal
# k1=np.min(arr,axis=1)  #vertical
# m1=np.min(arr,axis=0)   # horizontal
# print(m)
# print(k)
# print(m1)
# print(k1)










