#! /bin/python3

def bubble_sort(arr):
    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    arr = list(map(int, input('Enter the array elements in random order: ').split()))
    bubble_sort(arr)
    print(arr)
