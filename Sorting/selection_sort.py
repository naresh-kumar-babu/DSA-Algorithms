#! /bin/python3

def selection_sort(arr):
    for i in range(0, len(arr)-1):
    	min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_ind]:
            	min_ind = j
        arr[min_ind], arr[j] = arr[j], arr[min_ind]

if __name__ == '__main__':
    arr = list(map(int, input('Enter the array elements in random order: ').split()))
    selection_sort(arr)
    print(arr)
