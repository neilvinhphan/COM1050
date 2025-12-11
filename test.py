a = [97]

def lst_check(A):
    for _ in A:
        if _ == 1:
            continue
        else:
            return False
    return True

def len_check(a):
    count = 0
    while lst_check(a) == False:
        for i in range(len(a)):
            if a[i] == 1:
                count += 1
            elif a[i] % 2 == 0:
                count += 1
                a[i] //= 2
            else:
                count += 1
                a[i] = a[i]*3 + 1

    return count

print(len_check(a))
