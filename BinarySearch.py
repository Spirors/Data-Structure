def binarysearch(arr, val):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = int((left+right)/2)
        if val < arr[mid]:
            right = mid-1
        elif val > arr[mid]:
            left = mid+1
        else:
            return mid

def main():
    arr = [1,4,5,6,7,10,12,13]
    print(binarysearch(arr, 12))

if __name__ == '__main__':
	main()
