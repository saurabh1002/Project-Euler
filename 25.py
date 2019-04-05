# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

a = 1   # First Term of Fibonacci Sequence
b = 1   # Second Term of Fibonacci Sequence
c = 2
index = 3

while ((c % (10 ** 1000)) == (c % (10 ** 999))):

    a = b
    b = c
    c = a + b
    index = index + 1

print index
