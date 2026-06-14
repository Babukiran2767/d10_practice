'''
File handling:
----------------
File handling is the process of adding, removing,modifying or managing
the file with a programming language.

1) Open(file_Location/file_name,mode)
2) Read/write
3) Close 

--------------
1) Text File -> Text Data
2) Binary File -> audious,videos,jpg's,pdf's

r -> read
w -> write
a -> append
x -> exclusive

mod read:
--------
1) read()
2) readline()
3) realines()

'''


# f = open('data.txt','r')
# context = f.read(3)
# print(context)
# f.close()

# f=open('data.txt','r')
# context = f.readline()
# print(context,end='')
# # context = f.readline()
# # print(context)


# f=open('data.txt','r')
# context = f.readlines()
# print(context)

# f = open ('data.txt','r')
# context = f.readlines(14)
# print(context)


'''
mod write:
---------

1) write() over write by preveous data
2) writelines
'''

# f = open('data.txt','w')
# f.write('kiran')
# print('data added')


# f= open('data.txt','w')
# f.writelines(['how r u...?\n','yela vunav...?\n','bane vunanu'])
# print('data added')

# f= open('data1.txt','w')
# f.writelines(['how r u...?\n','yela vunav...?\n','bane vunanu'])
# print('data added')
'''
apppend

'''

# f = open('data.txt','a')
# f.write('evarra merantha...!\n')
# f.write('flutu jinka mundhu vudhu simham mundhu kadhu\n')
# f.write('arey entra idhi..!')

'''
exclusive

'''

# f = open('data2.txt','x')  #new file added



# f =open('data.txt','r')
# print(f.writable())
# print(f.readable())

# f =open('data.txt','r')
# print(f.read())
# print(f.closed)
# f.close()
# print(f.closed())



"""
combination of Modes:
----------------
r+  -> read + write
w+  -> write + read
a+  -> append + read
# """

# f=open('data.txt','r+')
# print(f.tell())
# print(f.read())
# print(f.tell())
# f.write('munny mishal')

# f=open('data.txt','w+')
# f.write('kiran babu')
# print(f.read())

# f=open('data.txt','w+')
# f.write('kiran weds munny')
# print(f.read())

with open ('data.txt','r') as f:
    print(f.read())