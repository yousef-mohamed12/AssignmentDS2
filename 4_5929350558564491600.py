import random
import time

def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        minimum =i
        for j in range(i+1,n):
            if a[j]<a[minimum]:
                minimum=j
        a[i], a[minimum] = a[minimum], a[i]
    return a



def bubble_sort(a):
    n=len(a)
    for i in range(n-1):
        flag=0
        for j in range(n-1-i):
            if a[j]>a[j+1]:
                flag=1
                a[j],a[j+1]=a[j+1],a[j]
        if flag==0:
            break
    return a




def insertion_sort(a):
    n=len(a)
    for i in range(1,n):
        j=i
        key=a[i]
        while j>0 and a[j-1]>key :
            a[j]=a[j-1]
            j=j-1
        a[j]=key
    return a




def tester_sort(x):
    base = [random.randint(0, 1000) for _ in range(x)]
    print(f"Array of size: {len(base)}")


    arr = base.copy()
    start = time.perf_counter()
    insertion_sort(arr)
    print(f"Insertion took : {time.perf_counter() - start:.6f} seconds")


    arr = base.copy()
    start = time.perf_counter()
    bubble_sort(arr)
    print(f"Bubble took    : {time.perf_counter() - start:.6f} seconds")


    arr = base.copy()
    start = time.perf_counter()
    selection_sort(arr)
    print(f"Selection took : {time.perf_counter() - start:.6f} seconds")

for i in range(5000,100001,5000):
    tester_sort(i)




