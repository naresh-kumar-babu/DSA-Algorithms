#Quick sort
def quicksort(a,i,j):
  if len(a)==1:
    return a
  if i<j:
    d = partition(a,i,j)
    quicksort(a,i,d-1)
    quicksort(a,d+1,j)

def partition(a,i,j):
  pivot = j
  j-=1
  while i<j:
    while a[i]<a[pivot]:
      i+=1
    while a[j]>a[pivot]:
      j-=1
    if i<j:
      a[i],a[j]=a[j],a[i]
  a[i],a[pivot]=a[pivot],a[i]
  return i
    

a = list(map(int,input().split()))
quicksort(a,0,len(a)-1)
print(a)
