#Linear Search
a = list(map(int,input().split()))
val = int(input("Enter the search value:"))
i = 0
while(i<len(a)):
  if a[i] == val:
    print(i)
    break
  i+=1
if i >= len(a):
  print("Value not found")
