def bubblesort(a):
     n = len(a)
     for i in range(n-2):
       for j in range(n-2-i):
         if a[j]>a[j+1]:
          temp = a[j]
          a[j] = a[j+1]
          a[j+1] = temp
x = [34,46,43,27,57,41,45,21,70]
print("Before sorting:",x)
bubblesort(x)
print("After sorting:",x)