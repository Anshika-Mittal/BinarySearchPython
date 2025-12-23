from util import time_it

def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1

if __name__ == '__main__':
    numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_find = 15  

    index = binary_search(numbers, number_to_find)
    ele = []
    i = index
    while i>=0:
        if numbers[i]==number_to_find:
            ele.append(i)
            i-=1
        else:
            break
    ele.reverse()
    i = index+1
    while i<len(numbers):
        if numbers[i]==number_to_find:
            ele.append(i)
            i+=1
        else:
            break
    print(f"Number found at indices {ele} using binary search")