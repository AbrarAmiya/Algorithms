file_in = open("/content/input1b.txt", 'r')
test_case = int(file_in.readline())

arr = []

for _ in range(test_case):
    line = file_in.readline()
    line = list(map(str, line.split()))
    arr.append(line)

print(arr)
output = open("/content/output1b.txt", 'w')

for i in range(len(arr)):
    operation = arr[i]
    if operation[2] == '+':
        output.write("The result of " + operation[1] + ' ' + operation[2] + ' ' + operation[3] + ' is ' + str(int(operation[1]) + int(operation[3])) + '\n')
    elif operation[2] == '-':
        output.write("The result of " + operation[1] + ' ' + operation[2] + ' ' + operation[3] + ' is ' + str(int(operation[1]) - int(operation[3])) + '\n')
    elif operation[2] == '*':
        output.write("The result of " + operation[1] + ' ' + operation[2] + ' ' + operation[3] + ' is ' + str(int(operation[1]) * int(operation[3])) + '\n')
    elif operation[2] == '/':
        output.write("The result of " + operation[1] + ' ' + operation[2] + ' ' + operation[3] + ' is ' + str(int(operation[1]) / int(operation[3])) + '\n')
    elif operation[2] == '^':
        output.write("The result of " + operation[1] + ' ' + operation[2] + ' ' + operation[3] + ' is ' + str(int(operation[1]) ** int(operation[3])) + '\n')
    else:
        output.write("Invalid operator: " + operation[2] + '\n')

file_in.close()
output.close()
