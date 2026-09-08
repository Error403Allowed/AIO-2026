import sys

def solve():
    # Read all tokens from stdin
    input = sys.stdin.read
    data = input().split()

    if not data:
        return

    n = int(data[0])
    a = [int(x) for x in data[1:n+1]]

    # Find starting position of the minimum element
    min_idx = a.index(min(a))

    # Check if array is strictly increasing starting from min element (with wrap-around)
    for i in range(n - 1):
        current_idx = (min_idx + i) % n
        next_idx = (min_idx + i + 1) % n

        if a[next_idx] <= a[current_idx]:
            print("NO")
            return
        
    print("YES")

if __name__ == "__main__":
    solve()
