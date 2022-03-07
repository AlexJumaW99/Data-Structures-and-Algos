# Author: Alex Juma 

'''
Steps:
1 - split array to left and right sub-arrays, do this recursively 
2 - sort the sub arrays
3 - merge them together into one big array again 
4 - Voila!
'''

def merge_sort(arr):
    if len(arr) > 1:
        #split arr to left and right arr 
        l_arr = arr[:len(arr)//2]
        r_arr = arr[len(arr)//2:]

        #recursion
        merge_sort(l_arr)
        merge_sort(r_arr)

        #create index vars
        i = 0 #left array 
        j = 0 #right array
        k = 0 #merged array

        #sorting 
        while i < len(l_arr) and j < len(r_arr): #while they both still have elements
            if l_arr[i] < r_arr[j]:
                arr[k] = l_arr[i]
                i += 1
            
            else:
                arr[k] = r_arr[j]
                j += 1
            
            k += 1
        
        while i < len(l_arr): #in case there are still elements in the left array but right array is exhausted
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr): #same as above but vice versa
            arr[k] = r_arr[j]
            j += 1
            k += 1
    
    return arr

arr = [12,34,55,85,2,455,892,3,9]
print(merge_sort(arr))