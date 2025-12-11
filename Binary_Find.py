lst = list(map(int, input().split()))
q = int(input())

def check(A, x):
    start = 0
    end = len(A)

    while start <= end:
        mid = (start + end)//2
        if A[mid] == x:
                return True
        if A[mid] > x:
            end = mid - 1
        elif A[mid] < x:
            start = mid + 1

    return False

print(check(lst, q))