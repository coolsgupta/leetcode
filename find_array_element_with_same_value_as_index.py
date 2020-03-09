def binarySearch(arr, l, r):
    while l <= r:

        mid = int(l + (r - l) / 2)

        # Check if x is present at mid
        if arr[mid] == mid + 1:
            return mid

            # If x is greater, ignore left half
        elif arr[mid] < mid + 1:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element was not present
    return -1

arr = [-10,-9,-7,-5,1,2,3,4,7,10,15,17,20,21,22]
i = binarySearch(arr,0,len(arr) -1)
print(i+1, arr[i])
