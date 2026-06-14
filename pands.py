# ============= 09-06-2026=================

# pandas

# ========================

# stu_details = [{
#     'stu1':{'name':'kiran','marks':89,'place':'hyd'},
#     'stu2':{'name':'munny','marks':79,'place':'che'},
#     'stu3':{'name':'mahesh','marks':80,'place':'bnr'}}
# ]

# print(stu_details)


import pandas as pd

# Series - > ID Array
# DataFrames -> 2D Array

# lst = [1,2,3,4,5]
# s = pd.Series(lst)
# # print(s)
# s.name="kiran"

# print(s.name)
# print(s.index)
# print(s.shape)
# print(s.size)
# print(s.dtype)
# print(s.head(8))
# print(s.tail(2))

# ========================================

# Basic Information
# s.head()      
# s.tail()   
# astype() 
# s.shape       
# s.size       
# s.dtype       
# s.index 
# name
# value
# index     

# Statistical Methods
# s.sum()      
# s.mean()      
# s.median()   
# s.min()       
# s.max()      
# s.std()      
# s.var()     
# s.count()     

# Value-related Methods
# s.unique()       
# s.nunique()       
# s.value_counts()  
# duplicated

# Sorting
# s.sort_values() 
# s.sort_index()    

# Missing Values
# s.isnull()        
# s.notnull()      
# s.dropna()        
# s.fillna(0)       

# Indexing
# s.iloc[0]         
# s.loc[0]

data ={

    'name':['kiran','vera','vijay','satish'],
    'age' :[23,24,25,23],
    'place':['mdp','kkd','rpm','viazg']
}

df = pd.DataFrame(data)
print(df)




