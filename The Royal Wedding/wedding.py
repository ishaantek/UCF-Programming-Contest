import math

def solve():
    inp = input().strip().split()
    A = int(inp[0])
    P = int(inp[1])
    
    perimeter = 2 * math.sqrt(math.pi * A)
    cost = P * perimeter
    
    print(f"{cost:.2f}")

if __name__ == "__main__":
    solve()