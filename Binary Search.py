def binarysearch (a, key):
  low = 0
  high = len(a) - 1
  while low <= high:
    mid = (high + low) // 2
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        high = mid - 1
    else:
        low = mid + 1
    return -1
a = [13,24,35,46,57,68,79]
print("the array elements are:",a)
k = int(input("enter the key element to search:"))
r = binarysearch(a,k)
if r == -1:
   print("Search UnSuccessful")
else:
   print("Search Successful key found at location:",r+1)