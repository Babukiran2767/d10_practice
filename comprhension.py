# lst=[f'{i} even' if i%2==0 else f'{i} odd'for i in range(1,11)]
# print(lst)


# lst=[i**2 for i in range (1,6) if i%2==0]
# print(lst)


# v='python'
# lst=[i.upper() for i in v]
# print(lst)

# words=["python","kiran","two"]
# lst=[len(i) for i in words]
# print(lst)


def fact(n):
    if n==0 or n==1:
        return n
    else:
        return n* fact(n-1)
x=fact(5)
print(x)