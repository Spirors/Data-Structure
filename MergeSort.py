def merge(arr, L, R):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1

def mergesort(arr):
    if len(arr) > 1:
        m = int(len(arr)/2)
        L = arr[:m]
        R = arr[m:]

        mergesort(L)
        mergesort(R)

        merge(arr, L, R)

def main():
    print("init")
    arr = [38, 27, 43, 3, 9, 82, 10]
    mergesort(arr)
    print(arr)

if __name__ == '__main__':
	main()
