#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      PC814
#
# Created:     12/02/2025
# Copyright:   (c) PC814 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Python program for Linear Search using iterative approach
def linear_search(arr, target):
    # Traverse through all elements in the array
    for index in range(len(arr)):
        # If the element is found, return its index
        if arr[index] == target:
            return index
    return -1

# Example usage:
arr = [10, 23, 45, 70, 11, 15]
target = 70

# Function call
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")
