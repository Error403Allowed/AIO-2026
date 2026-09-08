import sys

def solve():
    # Read all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    V = [int(x) for x in input_data[1:N+1]]

    max_vol = [0] * N
    
    # Left-to-right pass: cap each element by previous element + 1
    current = 0
    for i in range(N):
        current = min(V[i], current + 1)
        max_vol[i] = current

    # Right-to-left pass: propagate restrictions backward
    for i in range(N - 2, -1, -1):
        max_vol[i] = min(max_vol[i], max_vol[i+1] + 1)

    print(sum(max_vol))

if __name__ == '__main__':
    solve()
