def insertionsort(a):
    n = len(a)
    for i in range(1,n-1):
       v=a[i]
       j = i-1
       while j>=0 and a[j]>v:
          a[j+1] = a[j]
          j=j-1
          a[j+1] = v
x = [34,46,43,27,57,41,45,21,70]
print("Before sorting:",x)
insertionsort(x)
print("After sorting:",x)