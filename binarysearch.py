def linear_search(number_list, number_to_find):
    for index, elements in enumerate(number_list):
        if elements==number_to_find:
            return index
    return -1

def binary_search(number_list, number_to_find):
    left_index=0
    right_index=len(number_list)-1
    mid_index=0

    while left_index<=right_index:
        mid_index=(left_index+right_index)//2
        mid_number=number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        if mid_number<number_to_find:
            left_index=mid_index+1
        else:
            right_index=mid_index-1

    return -1

def binary_search_recursion(number_list, number_to_find, left_index, right_index):
    if right_index<left_index:
        return -1
    
    mid_index=(left_index+right_index)//2
    mid_number=number_list[mid_index]

    if mid_number==number_to_find:
        return mid_index
    if mid_number<number_to_find:
        left_index=mid_index+1
    else:
        right_index=mid_index-1
    return binary_search_recursion(number_list, number_to_find, left_index, right_index)

if __name__ == "__main__":
    number_list=[12,14,16,18,20,22,24]
    number_to_find=20

    index=binary_search_recursion(number_list, number_to_find, 0, len(number_list))
    print(f"The index {index} using binary search recursion")