def sequence_of_numbers(n):
    num = 1
    while num <= n:
        print(num)
        num = num * 2 + 1

n = int(input())

sequence_of_numbers(n)