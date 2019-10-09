def insertion_sort(arr):
    n = len(arr)

    # range from 1 to n
    for i in range(1, n):
        # [7|2, 4 1, 5, 3], left: sorted, right: unsorted
        tmp = arr[i]
        slot = i

        # Use while loop to shift element greater than "tmp"
        print(arr)
        while slot > 0 and arr[slot - 1] > tmp:
            arr[slot] = arr[slot - 1]
            print("{}, tmp:{}, slot:{}".format(arr, tmp, slot))
            slot -= 1
        # Insert
        arr[slot] = tmp
        print(slot)
        print(arr)
        print('----------------')
    return arr


if __name__ == '__main__':
    numbers = [7, 2, 4, 1, 5, 3]
    # numbers = [5, 4, 3, 2, 1, 0]
    sorted_list = insertion_sort(numbers)
    print(sorted_list)
