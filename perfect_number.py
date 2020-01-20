def perfect_number(num):
    if num <= 1:
        return False
    sum = 0
    for i in range(1, int(num/2)+1):
        if num % i == 0:
            sum += i
    return sum == num

print(perfect_number(28))

def print_perfect_nums(num):
    if num <= 1:
        return False
    for i in range(1, num+1):
        sum = 0
        for x in range(1, i):
            if i % x == 0:
                sum += x
        if sum == i:
            print(i)

print_perfect_nums(500)