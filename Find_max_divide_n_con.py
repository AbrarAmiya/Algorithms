# -*- coding: utf-8 -*-
"""Task 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1H7GqxZ7aMd34KJMKDzVkJP3K3GmOI4eB
"""

def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        if arr[0] >= arr[1]:
            return arr[0]
        else:
            return arr[1]
    else:
        mid = len(arr) // 2
        left_max = find_max(arr[:mid])
        right_max = find_max(arr[mid:])
        if left_max >= right_max:
            return left_max
        else:
            return right_max

input_file = open("/content/input4.txt", mode= "r")
output_file = open ("/content/output4.txt", mode = "w")

input_lines = input_file.readlines()
N = int(input_lines[0].strip())

print("Size of the array: ",N)

array1 = [int(num) for num in input_lines[1].split()]

print("Array: ",array1)

print("...")

max_of_array = find_max(array1)
print("Max Value: ",max_of_array)

output_file.write(str(max_of_array))

output_file.close()