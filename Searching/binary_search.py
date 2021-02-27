#Binary Search
a = list(map(int,input().split()))
val = int(input("Enter the search value:"))
low = 0
upp = len(a)-1
while(low<=upp):
  mid = (low+upp)//2
  if a[mid] == val:
    print("Found : ".format(mid))
    break
  elif a[mid] > val:
    upp = mid-1
  else:
    low = mid+1
if low>upp:
  print("Value not found")
