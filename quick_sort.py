# -*- coding: utf-8 -*-
"""Quick_sort.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n0ccq1DmjkBZERaDhnxcabzV7SgD5zka
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)




input= open("input3.txt", "r")
N = int(input.readline().strip())
numbers = []
numbers_line = input.readline().strip().split()
for i in range(N):
    numbers.append(int(numbers_line[i]))

quickSort(numbers, 0, N - 1)

output_str = ""
for i in range(N):
    output_str += str(numbers[i])
    if i != N - 1:
        output_str += " "

with open("output3.txt", "w") as file:
    file.write(output_str)