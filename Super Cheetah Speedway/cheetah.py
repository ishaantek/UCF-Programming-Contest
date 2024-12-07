m, s = map(int, input().split())

if s > m:
    print("he's cheetah-ing!")
elif s < m/2:
    print("slowpoke spotted!")
else:
    print("born to run!")