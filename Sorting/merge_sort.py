#Merge sort
def mergesort(a):
  if len(a)>1 :
    mid = len(a)//2
    firsthalf,secondhalf=a[:mid],a[mid:]
    mergesort(firsthalf)
    mergesort(secondhalf)
    merge(a,firsthalf,secondhalf)

def merge(a,firsthalf,secondhalf):
  i=j=0
  del a[:]
  while (i<len(firsthalf) and j<len(secondhalf)):
    if firsthalf[i]<secondhalf[j]:
      a.append(firsthalf[i])
      i+=1
    else:
      a.append(secondhalf[j])
      j+=1
  while (i<len(firsthalf)):
    a.append(firsthalf[i])
    i+=1
  while (j<len(secondhalf)):
    a.append(secondhalf[j])
    j+=1

a = list(map(int,input().split()))
print("Given Array")
print(a)
mergesort(a)
print("Sorted Array")
print(a)
