n = int(input())
p = list(map(int, input().split()))

# Find max gap between consecutive elements
longest = 0
for i in range(1, n):
    jump = p[i] - p[i - 1]
    if jump > longest:
        longest = jump

print(longest)
