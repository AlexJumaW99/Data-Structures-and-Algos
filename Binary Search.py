'''
Steps:
1 - Sort the array
2 - Set the interval to the length of the array 
3 - If the target is less than the mid value of the interval, consider lower half
4 - If target is equal to mid value, take mid value
5 - Else, consider higher half 
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
