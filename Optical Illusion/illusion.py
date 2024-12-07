n, L, R = map(int, input().split())
arr = list(map(int, input().split()))

L -= 1
R -= 1

arr[L:R+1] = reversed(arr[L:R+1])

print(' '.join(map(str, arr)))
