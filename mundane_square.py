import sys

def solve():
    # Fast input reading for CP
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    # Parse inputs
    N = int(input_data[0])
    K = int(input_data[1])

    R = [int(x) for x in input_data[2:2+N]]
    C = [int(x) for x in input_data[2+N:2+2*N]]

    # Quick sum check
    if sum(R) != sum(C):
        print("NO")
        return

    grid = [[0] * N for _ in range(N)]
    rem_R = R[:]
    rem_C = C[:]

    if K == 1:
        # Binary grid greedy approach
        for i in range(N):
            # Sort columns by highest remaining capacity
            cols = sorted(range(N), key=lambda j: rem_C[j], reverse=True)
            for j in range(rem_R[i]):
                col_idx = cols[j]
                if rem_C[col_idx] > 0:
                    grid[i][col_idx] = 1
                    rem_C[col_idx] -= 1
                else:
                    print("NO")
                    return
            rem_R[i] = 0

    else:
        # Non-binary grid approach
        for i in range(N):
            for j in range(N):
                val = min(rem_R[i], rem_C[j])
                grid[i][j] = val
                rem_R[i] -= val
                rem_C[j] -= val

    # Verify everything was filled properly
    if any(r != 0 for r in rem_R) or any(c != 0 for c in rem_C):
        print("NO")
        return

    # Print construction
    print("YES")
    for row in grid:
        print(*(row))

if __name__ == "__main__":
    solve()
