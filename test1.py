num = abs(int(input()))
k = input()
base = len(str(k))


def dec_to(num, base):
    dec_to.table = '0123456789ABCDEF'
    r = ''
    while num:
        num, y = divmod(num, base)
        r = dec_to.table[y] + r
    return r


def other_to_dec(num, base):

    while num > 0:
        num, y = divmod(num, base)


print(len(str(num)))
print(dec_to(num, base))
print(other_to_dec(num, base))
