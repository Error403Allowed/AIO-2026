import sys 

def solve():
    # Read input from stdin
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    K = int(input_data[1])
    D = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]

    C = [0] * N
    window_sum = 0
    total_spent = 0

    # Sliding window greedy strategy
    for i in range(N):
        # Remove element falling out of the length-K window
        if i >= K:
            window_sum -= C[i - K]

        # Greedy choice: cap current value so window sum doesn't exceed D
        max_allowed = D - window_sum
        C[i] = max(0, min(A[i], max_allowed))

        window_sum += C[i]
        total_spent += C[i]

    print(total_spent)

if __name__  == '__main__':
    solve()
