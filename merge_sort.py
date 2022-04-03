def merge_list(a, b): # merge function

    n1 = len(a)
    n2 = len(b)
    sorted_list = []    
    i, j = 0, 0

    while i < n1 and j < n2:

        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1

        else:
            sorted_list.append(b[j])
            j += 1 
    sorted_list += a[i:] + b[j:]
    return sorted_list

def split_list(array):
    
    N = len(array) // 2
    a1 = array[:N]
    a2 = array[N:]

    if len(a1) > 1:
        a1 = split_list(a1)

    if len(a2) > 1:
        a2 = split_list(a2)

    return merge_list(a1, a2)

result = split_list([9, 5, -3, 4, 7, 8, -8])

print(result)
