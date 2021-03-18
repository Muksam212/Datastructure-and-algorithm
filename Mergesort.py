def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted(left, right,arr)

def merge_two_sorted(a,b, arr):
    len_a=len(a)
    len_b=len(b)

    i=j=k=0

    while i<len_a and j<len_b:
        if a[i]<=b[j]:
            arr[k]=a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1


    while i<len_a:
        arr[k]=a[i]
        i+=1
        k+=1

    while j<len_b:
        arr[k]=b[j]
        j+=1
        k+=1

if __name__ == "__main__": 
    arr=[20,19,18,17,16,15,14,13,12,11]
    merge_sort(arr)
    print(arr)