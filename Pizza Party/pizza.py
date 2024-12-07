import math

def solve():
    n, s = map(int, input().split())
    angles = [int(input()) for _ in range(n)]
    
    all_angles = []
    for a in angles:
        all_angles.append(a % 360)
        all_angles.append((a + 180) % 360)
        all_angles.sort()
    
    slice_angles = []
    for i in range(2*n - 1):
        slice_angles.append(all_angles[i+1] - all_angles[i])
    slice_angles.append((360 + all_angles[0]) - all_angles[-1])

    extended = slice_angles + slice_angles
    window_size = n
    current_sum = sum(extended[0:window_size])
    max_sum_angle = current_sum
    
    for i in range(window_size, 2*n + (window_size - 1)):
        current_sum += extended[i] - extended[i - window_size]
        if current_sum > max_sum_angle:
            max_sum_angle = current_sum
    
    max_area = (max_sum_angle / 360.0) * math.pi * (s**2)
    
    print(max_area)

if __name__ == "__main__":
    solve()
