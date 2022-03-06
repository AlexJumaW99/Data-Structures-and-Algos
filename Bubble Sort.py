#In-efficient in the real world compared to other sorting algos
#Time complexity - Ranges from O(n) to O(n**2)
#Space complexity - always remains the same, no additional space needed ever

'''
Steps:
1 - Iterate through list
2 - If el in index i > el in i+1, then swap them 
3 - Break loop when list is sorted
'''

arr = [23,35,11,87,3,6,99,34]

def bubble_sort(arr):
    sorted = False

    while not sorted:
        sorted = True

        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

print(bubble_sort(arr))


