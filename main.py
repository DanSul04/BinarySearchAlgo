# Adapted Binary Search Algorithm From Class:

def binSearch(A, start, end, k): 
    if start > end:
        return None

    mid = (end + start) // 2
    print(f"Checking subarray: {A[start:end+1]}") # print current subarray
    print(f"Middle index: {mid}, Middle value: {A[mid]}") # middle index and element

    if (A[mid] == k):
        return mid
        print(f"The middle element is {mid}")
    elif (A[mid] < k):
        return binSearch(A, start, mid - 1, k) # go left in descending
    else:
        return binSearch(A, mid + 1, end, k) # go right in descending
        print(f"The subarray, from start to end is {binsearch}:")

# Array
A = [99, 67, 56, 51, 44, 39, 38, 23, 21, 17, 11, 2]  # test case 1

# Searching for an element
k = 44 # test case 1
print(f"\nSearching for {k}...")
index = binSearch(A, 0, len(A) - 1, k)
if index is not None:
    print(f"Found {k} at index {index}")
else:
    print(f"{k} is not in the array")
