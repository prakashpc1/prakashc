def mergesort(a,l,h):
    if l<h:
        m=l+(h-l)//2
        mergesort(a,l,m)
        mergesort(a,m+1,h)
        combine(a,l,m,h)
def combine(a,l,m,h):
    n1=m-l+1
    n2=h-m
    L=[0]*(n1)
    R=[0]*(n2)
    for i in range (0,n1):
        L[i]=a[l+i]
    for j in ragne(0,n2):
        R[j] = a[m+1+j]
        i=0
        j=0
        k=1
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                a[k]=L[i]
                i+=1
            else:
                a[k]=R[j]
                j+=1
            k+=1
        while i<n1:
            a[k] = L[i]
            i += 1
            k += 1
            while j < n2:
                a[k] = R[j]
            j += 1
            k += 1
            x = [34, 46, 43, 27, 57, 41, 45, 21, 70]
            print("Before sorting:", x)
            mergesort(x, 0, len(x) - 1)
            print("After sorting:", x)