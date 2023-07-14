# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MRl0NqhFtHnns0tYmfSW2vPdB0z244k9
"""

def merge(arr1, arr2, count):
    merged_arr = []
    current_count = count
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            merged_arr.append(arr2[j])
            current_count += len(arr1) - i
            j += 1
        else:
            merged_arr.append(arr1[i])
            i += 1

    merged_arr.extend(arr1[i:])
    merged_arr.extend(arr2[j:])

    return merged_arr, current_count


def AlienCount(arr, count=0):
    if len(arr) == 1:
        return arr, count

    mid = len(arr) // 2
    x, c1 = AlienCount(arr[:mid], count)
    y, c2 = AlienCount(arr[mid:], count)

    merged_arr, current_count = merge(x, y, c1 + c2)

    return merged_arr, current_count


###
input= open("input1.txt", "r")
N = int(input.readline().strip())
heights = []
heights_line = input.readline().strip().split()
for i in range(N):
    heights.append(int(heights_line[i]))
print("Number of Aliens: ",N)
print("Line of heights: ",heights)
sorted_arr, count = AlienCount(heights_line)
result = AlienCount(heights)
print(result)
with open("output1.txt", "w") as file:
    file.write(str(result))
input.close()