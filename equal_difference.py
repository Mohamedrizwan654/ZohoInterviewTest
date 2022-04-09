al = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26
}

v = input("Enter the string : ")
v = v.strip()
l = []
for i in range(0,len(v)):
    v1 = al[v[i]]
    #-al[i+1]
    if (i<len(v)-1):
        v2 = al[v[(i+1)]]
    #-al[-(i+1)]
    l.append(v1)
    l.append(v2)
l = sorted(list(set(l)),reverse = True)
m = []
for i in range(0,len(l)-1):
    v1 = l[i] - l[i+1]
    
    m.append(v1)

m = list(set(m))

if len(m)==1:
    print("Equal difference")
else:
    print("Unequal difference")


Question 6:

str = input("Enter the string : ")
str = str.strip()
l = []
for i in str:
    l.append(i)
l = list(sorted(l))
c = l[round(len(l)/2)]
a=[i for i in l if l.count(i)>1]
m = []
n = []
for i in a:
    m.append(i)
for i in sorted(a, reverse = True):
    n.append(i)
main = []
main.extend(m)
main.extend(n)
main.insert(round(len(main)/2), c)
mainStr = ""
for i in main:
    mainStr += i
    

print(mainStr)
