#! /bin/python3
# INSERTION SORT
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements of the array in random order: ').split()))
    insertion_sort(arr)
    print(arr)
