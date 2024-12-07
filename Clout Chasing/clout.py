n = int(input().strip())
best_name = ""
best_allit = -1
best_length = -1

for _ in range(n):
    first, last = input().strip().split()
    allit = 1 if first[0] == last[0] else 0
    total_len = len(first) + len(last)

    if allit > best_allit or (allit == best_allit and total_len > best_length):
        best_allit = allit
        best_length = total_len
        best_name = first + " " + last

print(best_name)
