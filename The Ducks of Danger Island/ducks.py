import sys

input_data = sys.stdin.read().strip().split()
n = int(input_data[0])
p = list(map(int, input_data[1:]))

q = [(100 - x)/100 for x in p]

q.sort(reverse=True)

expected = 0.0
current_product = 1.0


for i in range(n):
    expected += current_product
    current_product *= q[i]

print(expected)
