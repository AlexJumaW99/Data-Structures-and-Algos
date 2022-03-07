'''
A divide and conquer algo
Time complexity:
    Best case - O(n * log(n))
    Worst case - O(n**2)
'''


def quick_sort(arr, left, right):
    if left < right: #meaning there are at least 2 els in the array 
        pivot_pos = pivot(arr, left, right) #get the index of the pivot 

        #recursion
        quick_sort(arr, pivot_pos + 1, right) #carry out quicksort on right sub-array (right of pivot)
        quick_sort(arr, left, pivot_pos - 1) #carry out quicksort on left sub-array

def pivot(arr, left, right):
    i = left # index used to look for val bigger than pivot 
    j = right - 1 #index used to look for val smaller than pivot 
    piv = arr[right] #the value of the pivot 

    while i < j: #if they haven't passed each other 
        while i < right and arr[i] < piv:
            i += 1
        
        while j > left and arr[j] >= piv:
            j -= 1
        
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        
    if arr[i] > piv: #if a value bigger than the pivot was found, swap them. Then make the smaller value the new pivot
        arr[i], arr[right] = arr[right], arr[i]
    
    return i #return the position of the new pivot 
        
arr = [2635,23,56,99,2223,8,53,0,86,3]
(quick_sort(arr, 0, len(arr)-1))
print(arr)