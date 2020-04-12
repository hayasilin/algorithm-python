import sys

line = sys.stdin.readline()

# print(line)

input_list = []

for i in line:
  input_list.append(i)
  
input_list.sort(reverse=True)

for i in input_list:
  print(i, end='')