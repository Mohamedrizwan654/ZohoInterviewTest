v = input("Enter the string : ")
print("The distinct words are : ", end = ' ')
w = v.split()
res = []
for i in w:
    if i in res:
        pass
    else:
        res.append(i)
        print(i, end=' ')