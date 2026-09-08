import sys

def solve():
    # Read all inputs at once
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    A = [int(x) for x in input_data[2:2+N]]

    mid = N // 2

    # No operations allowed
    if K == 0:
        print(A[mid])
        return

    current_median = A[mid]

    # Try to raise elements from median up to the right boundary to match next element
    for i in range(mid, N - 1):
        count = i - mid + 1

        gap = A[i + 1] - A[i]
        needed = gap * count

        # If we have enough ops to bring all current elements up to A[i+1]
        if K >= needed:
            K -= needed
            current_median = A[i + 1]
        else:
            # Distribute remaining K evenly across the prefix group
            current_median += K // count
            K = 0
            break

    # If K still remains after reaching the end, boost all upper elements evenly
    if K > 0:
        count = N - mid
        current_median += K // count

    print(current_median)

if __name__ == '__main__':
    solve()
