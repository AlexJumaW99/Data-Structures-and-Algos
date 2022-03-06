'''
Steps:
1 - Compare x with the middle element.
2 - If x matches with the middle element, we return the mid index. 
3 - Else If x is greater than the mid element, recur for the right half as that's where it can be found.
4 - Else (x is smaller) recur for the left half.
'''

arr = [2, 3, 4, 10, 40]
x = 10

def bin_search(arr, bg, end, val):

    while bg < end: #as long as the beginning index is less than the ending index 
        mid = bg + (end-bg) // 2 #the middle index

        if arr[mid] == val:
            return mid

        elif arr[mid] > val:
            end = mid-1

        elif arr[mid] < val:
            bg = mid+1
        
        else:
            return '-1'

indx  = bin_search(arr, 0, len(arr)-1, 10)
print(f'The value {x}, is found in index {indx}.')
