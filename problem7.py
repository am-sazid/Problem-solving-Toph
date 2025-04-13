
N, M = map(int, input().split())
set1 = list(map(int, input().split()))
set2 = list(map(int, input().split()))

union_set = sorted(set(set1) | set(set2))

print(*union_set)



