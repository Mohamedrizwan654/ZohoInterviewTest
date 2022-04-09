no = int(input("Enter the number of string to be entered = "))
words = []
for i in range(no):
    words.append(input("Enter the string"+str(i+1)+" : "))

for i in words:
    print("String1 : "+''.join(sorted(i, reverse = True)))