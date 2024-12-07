import math

def count_palindromes(s):
    n = len(s)
    count = 0
    for center in range(n):
        l = r = center
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        l, r = center, center+1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count

def solve():
    K = int(input().strip())
    candidates = ["hspt", "abacaba"]

    for c in candidates:
        if count_palindromes(c) == K:
            print(c)
            return

    n = int((math.sqrt(1+8*K)-1)//2)
    big_run_pal = n*(n+1)//2
    leftover = K - big_run_pal

    result = []
    result.append('a' * n)

    if leftover > 0:
        pattern = ['b','c','d']
        for i in range(leftover):
            result.append(pattern[i % 3])

    password = "".join(result)
    print(password)

if __name__ == "__main__":
    solve()
