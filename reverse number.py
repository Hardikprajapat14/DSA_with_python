# Python equivalent of the given C++ code
n = int(input("Enter a number: "))
rev_num = 0

while n > 0:
    digit = n % 10
    rev_num = (rev_num * 10) + digit
    n = n // 10

print("Reversed number:", rev_num)
