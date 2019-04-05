def check_palindrome(num):
    integer = str(num)
    l = 0
    n = len(integer)-1
    if (integer[n] or integer[0]) == '0':
        return False
    if n == 0:
        return True
    while(n>=l):
        if(integer[l] != integer[n]):
            return False
        if l == n:
            return True
        l = l + 1
        n = n - 1
    return True

def dec_to_bin(num):
    list = ''
    while(num != 0):
        if (num % 2) == 0:
            list = '0' + list
            num = num / 2
        if (num % 2) == 1:
            list = '1' + list
            num = (num - 1) / 2
    return int(list)

list = []
for i in range (1, 1000000):
    if (check_palindrome(i)):
        list.append(i)
# print list

sum = 0
for a in list:
    bin = dec_to_bin(a)
    # print bin
    flag = check_palindrome(bin)
    if flag:
        # print ('true')
        sum = sum + a

print sum
