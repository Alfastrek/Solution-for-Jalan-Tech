def alternate_order(arr):
    positivelist=[]
    negativelist=[]
    finalarr=[]
    for i in range(len(arr)):
        if arr[i]<0:
            negativelist.append(arr[i])
        else:
            positivelist.append(arr[i])
    # TO PRINT
    i = 0
    j = 0
    while i < len(positivelist) and j < len(negativelist):
        finalarr.append(positivelist[i])
        finalarr.append(negativelist[j])
        i += 1
        j += 1
    
    # Append remaining elements if any
    while i < len(positivelist):
        finalarr.append(positivelist[i])
        i += 1
    
    while j < len(negativelist):
        finalarr.append(negativelist[j])
        j += 1

    return finalarr
        

# Example usage:
input_array = [-1,-2,-3,4,5,6,7,8]
output = alternate_order(input_array)
print(output)

#With space complexity O(1):
# def alternate_order(arr):
  
#     next_positive_index = 0
#     for i in range(len(arr)):
#         if arr[i] < 0:
#             arr[i], arr[next_positive_index] = arr[next_positive_index], arr[i]
#             next_positive_index += 2
#     return arr


# input_array = [-1, -2, -3, 4, 5, 6, 7, 8]
# output = alternate_order(input_array)
# print(output)