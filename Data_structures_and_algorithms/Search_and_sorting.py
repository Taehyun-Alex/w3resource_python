"""
# 1
Write a Python program for binary search.
Binary Search : In computer science, a binary search or half-interval search algorithm finds the position of a target value within a sorted array. The binary search algorithm can be classified as a dichotomies divide-and-conquer search algorithm and executes in logarithmic time.
Test Data :
binary_search([1,2,3,5,8], 6) -> False
binary_search([1,2,3,5,8], 5) -> True
"""


def binary_search(array, search_value):
    sorted_array = sorted(array)
    first = 0
    last = len(array) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if sorted_array[mid] == search_value:
            found = True
        else:
            if search_value < sorted_array[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


# print(binary_search([1, 2, 3, 5, 8, 10, 12, 40, 100], 1))


"""
# 2
Write a Python program for sequential search.
Sequential Search : In computer science, linear search or sequential search is a method for finding a particular value in a list that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.
Test Data :
Sequential_Search([11,23,58,31,56,77,43,12,65,19],31) -> (True, 3)
"""


def sequential_search(array, search_value):
    for x in range(len(array)):
        if array[x] == search_value:
            print(f"True, {x}")


sequential_search([11,23,58,31,56,77,43,12,65,19],65)