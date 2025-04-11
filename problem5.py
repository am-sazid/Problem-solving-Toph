# N = int(input())
# A = list(map(int, input().split()))

# for i in A:
#     if   A[i] > A[i - 1] and len(A) == N:
#         print("YES")
#     else:
#         print("NO")
N = int(input())
A = list(map(int, input().split()))

if len(A) != N:
    print("Invalid input")
    exit()

is_ascending = True

for i in range(1, N):
    if A[i] < A[i - 1]:
        is_ascending = False
        break

if is_ascending:
    print("Yes")
else:
    print("No")
