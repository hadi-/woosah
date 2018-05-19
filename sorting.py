__author__ = 'xhadix'
a = [3,3,1,2]
for j in range(len(a)):
    swapped = False
    index = False
    i = 0
    while i<len(a)-1:
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            swapped = True
        i = i+1
    if swapped == False:
        break
print (a, "\n")
print (index)