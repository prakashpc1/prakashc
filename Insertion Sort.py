def insertionsort(a):
    n = len(a)
    for i in range(1,n-1):
        k=a[i]
        j=i-1
        while j>=0 and a[j]>k:
            a[j+1] = a[j]
            j=j-1
            a[j+1]=k
x = [34,46,43,27,57,41,45,21,70]
print("Befroe sorting:",x)
insertionsort(x)
print("After sorint:",x)

