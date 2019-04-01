# What is the largest Palindrome which is a product of two 3 digit numbers?
def check_palindrome(num):
    integer = str(num)
    l = 0
    n = len(integer)-1
    while(n>1):
        if(integer[l] != integer[n]):
            return False
        l = l + 1
        n = n - 1
    return True

largest_pal = 0
for a in range (100, 1000, 1):
    for b in range(100, 1000, 1):
        if(check_palindrome(a*b)):
            if(largest_pal <= a*b):
                largest_pal = a*b
                num1 = a
                num2 = b

print(largest_pal, num1, num2)
