def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    n, k = map(int, input_data[0:2])
    sequences = input_data[2:]

    seq_set = set(sequences)

    chars = ['A', 'C', 'G', 'T']
    char_to_index = {c:i for i,c in enumerate(chars)}

    candidate = ['A'] * k

    def increment(seq_list):
        i = k - 1
        while i >= 0:
            idx = char_to_index[seq_list[i]]
            if idx < 3:  # Can increment
                seq_list[i] = chars[idx+1]
                return True
            else:
                seq_list[i] = 'A'
                i -= 1
        return False  

    while True:
        cand_str = ''.join(candidate)
        if cand_str not in seq_set:
            print(cand_str)
            break
        increment(candidate)

if __name__ == "__main__":
    solve()
